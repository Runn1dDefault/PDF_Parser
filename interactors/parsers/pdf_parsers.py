import os
import re
from abc import abstractmethod
from io import BytesIO
from typing import Iterator

from PyPDF2 import PdfReader

from interactors.constants import BASIC_HEADERS, HASH_HEADERS, CUSTOMER_STRING, END_HEADERS


class BasePDFParser:
    """
    The class responsible for reading tables from a file
    from point A to point B
    identifying the table by the Repair order number on the page
    """

    def __init__(self, filepath: str | os.PathLike = None,  bytes_io: BytesIO = None):
        assert filepath or bytes_io, 'You can pass either a path to a file or a BytesIO object'

        self.filepath = filepath
        self.pdf_bytes = bytes_io

    def _read_pdf_pages(self) -> Iterator[tuple[int, list[str]]]:
        reader = PdfReader(self.filepath or self.pdf_bytes)

        for page_index, page in enumerate(reader.pages):
            page_text = page.extract_text()
            yield page_index, page_text.split('\n')

    @abstractmethod
    def parse_tables(self) -> dict[str, list[str]]:
        pass


class PDFParser(BasePDFParser):
    def parse_tables(self) -> tuple[dict[str, list[str]], set[str]]:
        collected_tables = {}
        hash_tables_ids = set()  # here collect a table that starts with '#'

        for page_index, page_rows in self._read_pdf_pages():
            start_table_index = end_table_index = 0
            repair_order_num = None
            is_hash_table = False
            check_end_headers = False

            for row_index, row in enumerate(page_rows):
                if all(field in row for field in HASH_HEADERS):
                    start_table_index = row_index + 1
                    is_hash_table = True

                if all(field in row for field in BASIC_HEADERS):
                    start_table_index = row_index + 1

                if CUSTOMER_STRING in row:
                    repair_order_text = [value for value in row.split(CUSTOMER_STRING) if value.strip()][0].split()[-1]
                    repair_order_num = re.findall(r'\d+', repair_order_text)[0]
                    if len(repair_order_num) > 10:
                        repair_order_num = repair_order_num[-5:]

                    if row_index > 10:
                        end_table_index = row_index + 1
                        break
                    else:
                        check_end_headers = True

                if check_end_headers and all(field in row for field in END_HEADERS):
                    end_table_index = row_index
                    break

            if not repair_order_num:
                continue

            if end_table_index > start_table_index > 0:
                if not collected_tables.get(repair_order_num):
                    collected_tables[repair_order_num] = []

                collected_tables[repair_order_num].extend(page_rows[start_table_index:end_table_index])

            if is_hash_table:
                hash_tables_ids.add(repair_order_num)

        return collected_tables, hash_tables_ids
