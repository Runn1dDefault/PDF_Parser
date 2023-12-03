import os
from pathlib import Path

from interactors.parsers.pdf_parsers import PDFParser
from interactors.parsers.handlers import RowParser
from interactors.items import ExtractData


FILEPATH = os.path.join(Path(__file__).parent, 'static', 'BWO-675867.1_MBA_S_63e57158f33af.pdf')
PARSED_TABLE = {'675867': ['# A           9928    WSTAR CUSTOMER STATES THE PARKING BRAKE '
                           'INDICATOR IS ON,',
                           '                            REF LAST REPAIR',
                           '# B  99MB     9928    CM    PERFORM MERCEDES BENZ COURTESY '
                           'INSPECTION           ',
                           '                           001-989-33-03-09 HYPOID GEAR '
                           'OIL              (QTY 2)',
                           '                           001-989-33-03-09 HYPOID GEAR '
                           'OIL              (QTY 2)',
                           '                           000000-006365 HEXALOBULAR '
                           'BOLT               (QTY 16)',
                           '                           276-141-01-80 FLANGE '
                           'GASKET                   (QTY 6)',
                           '                           000-990-39-24 SCREW WITH '
                           'FEATURE             (QTY 12)',
                           '                           016-997-50-45 SEAL '
                           'RING                       (QTY 4)',
                           '                           003-989-98-20-10 SEALANT '
                           'MB                   (QTY 1)',
                           '                           166-423-02-81 PISTON '
                           'HOUSING                  (QTY 1)',
                           '                           000-989-56-05-11-0111 BRAKE '
                           'FLUID             (QTY 1)',
                           '                           276-200-03-70 BELT '
                           'TENSIONER                  (QTY 1)',
                           '                           276-202-01-19 GUIDE '
                           'PULLEY                    (QTY 1)',
                           '                           003-993-57-96 V RIBBED '
                           'BELT                   (QTY 1)',
                           '                           276-202-01-19 GUIDE '
                           'PULLEY                    (QTY 1)',
                           '                           018-990-00-01 '
                           'SCREW                           (QTY 4)',
                           '                           000-420-99-04 DISK BRAKE '
                           'PAD                  (QTY 1)',
                           '                           166-423-05-00 BRAKE DISC, '
                           'UNVENTED            (QTY 2)',
                           '                           220-421-01-71 PAN HEAD FIT '
                           'BOLT               (QTY 2)',
                           '# C  CW       9928    CM    COMPLIMENTARY EXTERIOR CAR WASH '
                           '($14.95 NO CHARGE TO',
                           '                            CUSTOMER, CHARGE TO SERVICE '
                           'GOODWILL). VACUUM OF    ',
                           '                            FRONT FLOORBOARDS '
                           'ONLY.                             675867                          '
                           'CUSTOMER #: 67404                                           ',
                           '# D *                 WSTAR TECH STATES CYLINDER HEAD FRONT '
                           'COVERS ARE LEAKING',
                           '# E *                 WM08  TECH NOTES THERE IS AN OIL LEAK AT '
                           'THE CAMSHAFT',
                           '                            ADJUSTER MAGNETS',
                           'COMPANY NAME              BENZ '
                           'ELW                                                  ',
                           'COMPANY '
                           'PHONE                                                                       ',
                           'POLICY NUMBER             BENZ '
                           'ELW                                                  ',
                           'POLICY TERM                     '
                           '84                                                  ',
                           'EFFECTIVE DATE         26 NOV '
                           '2016                                                  ',
                           'DEDUCTIBLE                    '
                           '0.00                                                  ',
                           'MILEAGE '
                           'LIMIT                                                                       ',
                           'BEGIN MILES                      '
                           '5                                                  ',
                           'END MILES                    '
                           '75000                                                  ',
                           'COMPONENTS                                                                          '
                           '675867                          CUSTOMER #: '
                           '67404                                           ']}

REPAIR_ORDER = '675867'
PARSED_ITEMS = [
    ExtractData(repair_order_number='675867',
                labor_operation='',
                labor_type='WSTAR'),
    ExtractData(repair_order_number='675867',
                labor_operation='99MB',
                labor_type='CM'),
    ExtractData(repair_order_number='675867',
                labor_operation='CW',
                labor_type='CM'),
    ExtractData(repair_order_number='675867',
                labor_operation='*',
                labor_type='WSTAR'),
    ExtractData(repair_order_number='675867',
                labor_operation='*',
                labor_type='WM08')
]


def test_read_table():
    pdf_parser = PDFParser(FILEPATH)
    tables, hash_tables = pdf_parser.parse_tables()
    assert tables == PARSED_TABLE
    assert REPAIR_ORDER in hash_tables
    return tables


def test_parse_items():
    table = test_read_table()
    items = []
    for _, rows in table.items():
        for row in rows:
            row_parser = RowParser(REPAIR_ORDER, row)
            item = row_parser.parse_hash_table_item()
            if item:
                items.append(item)

    assert all(item in PARSED_ITEMS for item in items)


def test_table_hash_lines():
    test_parse_items()


if __name__ == '__main__':
    test_table_hash_lines()
