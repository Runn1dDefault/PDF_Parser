import re
import time

from interactors.constants import END_HEADERS
from interactors.items import ExtractData
from interactors.utils import word_by_chars_num_to_last_letter, word_by_chars_num_to_first_letter


class LinesParser:
    """
    the class responsible for submitting the structural view of the table rows
    """
    def __init__(self, table_rows: list[str]):
        self.table_rows = table_rows

    def sort_table_rows(self):
        rows = []
        start_line = end_line = 0
        lines_count = len(self.table_rows)

        for line_index, line in enumerate(self.table_rows):
            if all(field in line for field in END_HEADERS) or lines_count == line_index + 1:
                # Required index to store the last line
                end_line = line_index
                break

            check_line = line.strip()
            if not check_line or len(check_line) <= 1:
                continue

            first_symbol = line[0].strip()
            if not first_symbol or not first_symbol.isalpha():
                continue

            second_symbol = line[1].strip()
            if second_symbol and second_symbol != '*':
                continue

            end_line = line_index
            row = self.table_rows[start_line:end_line]
            if row:
                rows.append(row)
            start_line = line_index

        last_row = self.table_rows[start_line:end_line]
        if last_row:
            rows.append(last_row)
        return rows


class RowParser:
    def __init__(self, repair_order: str, row_lines: list[str] | str):
        self.repair_order = repair_order
        self.row_lines = row_lines
        self._errors = {}

    @property
    def parse_errors(self):
        return self._errors

    def find_discounts_lines(self) -> list[tuple[str, str]]:
        start_index = None
        discounts_lines = []

        self.row_lines.append('LINE_END')
        for line_index, line in enumerate(self.row_lines):
            check_start_letter = not line.strip() or not line[0].strip()

            if check_start_letter:
                continue

            if start_index is None:
                start_index = line_index
                continue

            check_lines = self.row_lines[start_index:line_index]
            last_index = len(check_lines) - 1

            for check_line_index, check_line in enumerate(check_lines):
                next_line_index = check_line_index + 1

                if next_line_index > last_index:
                    break

                next_line = check_lines[next_line_index]
                next_line_values = [value.strip() for value in next_line.split() if value.strip()]
                if next_line_values and next_line_values[-1].startswith('-') and next_line.strip().startswith('LABOR'):
                    discounts_lines.append((next_line, line))

            start_index = line_index
        return discounts_lines

    def parse_items(self):
        discounts = self.find_discounts_lines()
        labor_operation = None
        found_items = False
        counter = 0

        for line_index, line in enumerate(self.row_lines):
            if found_items and line[0].strip():
                break

            if line.strip().startswith('LABOR') or line.strip().startswith('PARTS'):
                continue

            if not line[:5].strip() and line[5].strip():  # detecting OPCODE
                labor_operation = word_by_chars_num_to_first_letter(line, 6)
                continue

            if labor_operation is None or len(line) < 80 or line[:5].strip():  # detecting DIGITS LINE
                continue

            #  sometimes the TYPE field is concatenated with the previous field, it must be excluded
            #  the previous field is usually numbers,
            #  and the beginning of TYPE field is always letters
            labor_type = re.findall(r'[A-Z]+\d+|[A-Z]+', word_by_chars_num_to_last_letter(line, 21))
            if not labor_type:  # len(labor_type[0]) > 4
                continue

            checking_line = not line[:8].strip() and not line[9].strip() and line[8].isdigit()
            prev_line = self.row_lines[line_index - 1]
            prev_line_check = not prev_line[:8].strip() and not prev_line[9].strip() and prev_line[8].isdigit()
            if checking_line or prev_line_check:
                continue

            # some lines after DIGITS LINE are suitable for filters, but they need to be filtered out
            # if there is no OPCODE in this line, then there is usually always something before the TECH field
            if not line[5].strip() and len([word for word in line[:15].split() if word.strip()]) > 1:
                continue

            if self.repair_order in line:
                line = line.split(self.repair_order)[0]

            sale_amount = line.split()[-1]
            if '(N/C)' not in sale_amount and re.findall(r'[a-zA-Z]+', sale_amount):
                continue

            item = ExtractData(
                repair_order_number=self.repair_order,
                labor_operation=labor_operation,
                labor_type=labor_type[0],
                sale_amount=line.split()[-1],
                cost=word_by_chars_num_to_last_letter(line, 40)
            )

            sold_hours = word_by_chars_num_to_last_letter(line, 33)
            search_sold_hours = re.findall(r'\d+\.\d+', sold_hours)
            if search_sold_hours:
                item.sold_hours = search_sold_hours[0]

            if discounts and counter < len(discounts):
                discount_line, _ = discounts[counter]
                discount_line_values = [value.strip() for value in discount_line.split() if value.strip()]
                item.discount = discount_line_values[-1]

            counter += 1
            yield item
            found_items = True

        if labor_operation and not found_items:
            msg = '%s: Not found digits line in row: \n%s' % (self.repair_order, '\n'.join(self.row_lines))
            self._errors[time.mktime(time.localtime())] = msg
        elif not labor_operation and not found_items:
            msg = '%s: Not found data in row: \n%s' % (self.repair_order, '\n'.join(self.row_lines))
            self._errors[time.mktime(time.localtime())] = msg

    def parse_hash_table_item(self) -> ExtractData | None:
        # method for parsing items in a table where lines start with '#'
        assert isinstance(self.row_lines, str)

        opcode = word_by_chars_num_to_first_letter(self.row_lines, 6)
        if not opcode:
            # some start at position 5
            opcode = word_by_chars_num_to_first_letter(self.row_lines, 5)

        type_value = word_by_chars_num_to_first_letter(self.row_lines, 23)

        if type_value.strip():
            return ExtractData(
                repair_order_number=self.repair_order,
                labor_operation=opcode,
                labor_type=type_value,
            )
