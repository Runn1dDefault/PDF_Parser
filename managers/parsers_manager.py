import os
import time
import ntpath
from glob import glob
from uuid import uuid4
from io import BytesIO
from logging import getLogger
from datetime import datetime

import pandas as pd

from config import DESKTOP_PATH
from interactors.parsers.zip_extractor import ZipExtractor
from interactors.parsers.pdf_parsers import PDFParser
from interactors.parsers.handlers import RowParser, LinesParser
from interactors.items import ExtractData


class BaseDataFrameManager:
    # IGNORE_COLUMNS = ('filename',)
    IGNORE_COLUMNS = []

    def __init__(self, files: list[str | os.PathLike]):
        self.logger = getLogger(self.__class__.__name__)
        self.files = files
        self.out_xls_path = None
        self.df = pd.DataFrame()
        self.errors_df = pd.DataFrame({'filename': [], 'time': [], 'error': []})
        self.error_files = set()

    def _collect_data(self, item: ExtractData, filename: str) -> None:
        data = item.dict()
        data['filename'] = filename
        item_df = pd.DataFrame([data])
        
        if self.df.empty:
            self.df = item_df
        else:
            self.df = pd.concat([self.df, item_df], ignore_index=True)

    def _save_error(self, filename: str, error: str, err_time: time.struct_time = None) -> None:
        self.error_files.add(filename)
        error_time = time.asctime(time.localtime() if err_time is None else err_time)
        error_data = dict(error=[error], filename=[filename], time=[error_time])
        error_df = pd.DataFrame(error_data)

        if self.errors_df.empty:
            self.errors_df = error_df
        else:
            self.errors_df = pd.concat([self.errors_df, error_df], ignore_index=True)

    def data_ordering(self) -> None:
        pass

    @property
    def xls_filepath(self):
        filepath = os.path.join(DESKTOP_PATH, f'{datetime.now().date()}.xlsx')

        if os.path.exists(filepath):
            template_path = os.path.join(DESKTOP_PATH, f'{datetime.now().date()}(*).xlsx')
            saved_count = len(glob(template_path))
            filepath = os.path.join(DESKTOP_PATH, f'{datetime.now().date()}({saved_count + 1}).xlsx')

        return filepath

    def write_to_excel(self):
        self.logger.info('Writing results to xlsx...')
        self.data_ordering()

        save = False

        self.out_xls_path = self.xls_filepath

        with pd.ExcelWriter(self.out_xls_path, engine="xlsxwriter") as writer:
            if not self.df.empty:
                columns = {column: column.replace('_', ' ').title() for column in self.df.columns
                           if column not in self.IGNORE_COLUMNS}
                save = True
                self.df = self.df.rename(columns=columns)
                self.df.to_excel(writer, sheet_name="Output", index=False, columns=list(columns.values()))

            if not self.errors_df.empty:
                save = True
                self.errors_df.to_excel(writer, sheet_name="Errors", index=False)

            if save:
                self.logger.info('Saving data to xlsx...')
                writer.save()
            else:
                self.logger.error('Not found data for saving to xlsx!')


class ParserManager(BaseDataFrameManager):
    _filepath: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_id = str(uuid4())

    def run(self):
        self.logger.info('Start...')

        for file in self.files:
            self._filepath = file

            if file.endswith('.pdf'):
                self.logger.info('Will be parse pdf: ' + file)
                self.pdf_parse(file)

            elif file.endswith('.zip'):
                self.logger.info('Will be parse zip: ' + file)
                self.zip_parse(file)

        self.write_to_excel()
        self.logger.info('Over!')
        return self.task_id

    def parse(self, filepath_or_bytes, filename: str):
        pdf_parser = PDFParser(filepath_or_bytes)
        tables, hash_tables_ids = pdf_parser.parse_tables()

        for repair_order, table in tables.items():
            if repair_order in hash_tables_ids:
                for row_lines in table:
                    if not row_lines.strip() or not row_lines.startswith('#'):
                        continue

                    row_parser = RowParser(repair_order, row_lines)
                    item = row_parser.parse_hash_table_item()
                    if item:
                        self._collect_data(item, filename)

                continue

            sorted_rows = LinesParser(table).sort_table_rows()

            for row_lines in sorted_rows:
                row_parser = RowParser(repair_order, row_lines)

                for item in row_parser.parse_items():
                    self._collect_data(item, filename)

                for ts, error in row_parser.parse_errors.items():
                    self._save_error(filename, error=error, err_time=datetime.fromtimestamp(ts).timetuple())

    def pdf_parse(self, filepath: str) -> None:
        filename = ntpath.basename(filepath)
        try:
            self.parse(filepath, filename=filename)
        except Exception as e:
            self._save_error(filename=filename, error=str(e))
            self.logger.error(f'File: {filepath} Error: {e}')

    def zip_parse(self, filepath: str) -> None:
        zip_extractor = ZipExtractor(filepath)
        pdf_files = zip_extractor.get_files_by_format('pdf')

        if not pdf_files:
            return

        parsed_files = []

        for filename in pdf_files:
            if filename in parsed_files:
                continue

            parsed_files.append(filename)
            file_object = zip_extractor.extract_file(filename)
            try:
                self.parse(BytesIO(file_object.read()), filename=filename)
            except Exception as e:
                file_msg = f'Zip: {filepath.split("/")[-1]} File: {filename}'
                error = str(e)
                self._save_error(filename=file_msg, error=error)
                self.logger.error(file_msg + ' Error: ' + error)

    def _ordering_by_labor_type(self):
        if self.df.empty:
            return

        i_and_w_df = self.df.query('labor_type.str.startswith("I") or labor_type.str.startswith("W")', engine='python')

        if i_and_w_df.empty:
            self.logger.error('No labor type data that starts with I or W!')
            self.df = self.df.sort_values("repair_order_number")
            return

        for column in ('sold_hours', 'cost', 'sale_amount'):
            i_and_w_df[column] = ''

        df_with_sorted = i_and_w_df.sort_values("repair_order_number")

        df_without_i_and_w = self.df[~self.df['labor_type'].str.startswith("I", na=False) &
                                     ~self.df['labor_type'].str.startswith('W', na=False)]
        df_without_i_and_w_sorted = df_without_i_and_w.sort_values("repair_order_number")
        self.df = pd.concat([df_with_sorted, df_without_i_and_w_sorted], ignore_index=True)

    def _remove_errors_extract_data(self):
        if not self.error_files or self.df.dropna().empty:
            return

        self.df = self.df[~self.df['filename'].isin(self.error_files)]

    def data_ordering(self) -> None:
        self._remove_errors_extract_data()
        self._ordering_by_labor_type()
