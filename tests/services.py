from interactors.parsers.handlers import LinesParser, RowParser
from interactors.parsers.pdf_parsers import PDFParser


def test_parse(filepath, repair_order, parsed_table, sorted_rows, parsed_items):
    pdf_parser = PDFParser(filepath)
    tables, _ = pdf_parser.parse_tables()
    assert tables == parsed_table
    _sorted_rows = LinesParser(tables[repair_order]).sort_table_rows()
    assert sorted_rows == _sorted_rows

    items = []
    for row in _sorted_rows:
        row_parser = RowParser(repair_order, row)
        for item in row_parser.parse_items():
            items.append(item)

        assert not row_parser.parse_errors

    assert all(item in parsed_items for item in items)
