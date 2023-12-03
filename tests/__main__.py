from tests.test_read_discounts import test_discounts
from tests.test_table_lines_start_with_hash import test_table_hash_lines
from tests.test_table_without_parts_lines import test_table_without_parts_lines
from tests.test_single_row import test_single_row
from tests.test_multiply_items_from_one_row import test_multiple_items_from_one_row


def main():
    test_discounts()
    print('Test discounts: done!')
    test_single_row()
    print('Test single row: done!')
    test_table_without_parts_lines()
    print('Test table without parts lines: done!')
    test_multiple_items_from_one_row()
    print('Test multiply items from one row: done!')
    test_table_hash_lines()  # another table template
    print('Test table lines start with \'#\': done!')


if __name__ == '__main__':
    main()
