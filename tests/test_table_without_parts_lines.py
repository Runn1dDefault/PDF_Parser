import os
from pathlib import Path

from interactors.parsers.pdf_parsers import PDFParser
from interactors.parsers.handlers import LinesParser, RowParser
from interactors.items import ExtractData

FILEPATH = os.path.join(Path(__file__).parent, 'static', '214048.pdf')
PARSED_TABLE = {'214048': ['A CUSTOMER STATES VEHICLE IS SITTING LOW IN THE REAR END/CHECK '
                           'AND     ',
                           '        '
                           'ADVISE                                                         ',
                           '     15 STEERING/SUSPENSION                           ',
                           '           30461   CP  0.01  3.00   7500   52500                 '
                           '525.00   525.00',
                           '        1 84355910 (S)COMPRESSOR   29253   59676     0  596.76   '
                           '596.76   596.76',
                           '        1 13500114 (S)RELAY          938    2626     0   26.26    '
                           '26.26    26.26',
                           ' 117781 REAR LEVEL RIDE COMPRESSOR HAS INTERNAL FAULT 3.00 '
                           'REPLACED ',
                           ' LEVEL RIDE COMPRESSOR AND '
                           'RELAY                                        ',
                           'B PERFORM COMPLIMENTARY 27-POINT MULTI - POINT INSPECTION , PIT '
                           'STOP,  ',
                           '        AND CAR WASH '
                           'TREATMENT.                                        ',
                           '     MPVI PERFORM COMPLIMENTARY 27-POINT MULTI - POINT',
                           '          INSPECTION , PIT STOP, AND CAR WASH         ',
                           '          TREATMENT.                                  ',
                           '           30461  ISP  0.02  0.00      0       '
                           '0                   0.00     0.00',
                           ' 117781 PERFORM '
                           'MPI                                                 ',
                           'C** CUSTOMER STATES THE CHECK ENGINE LIGHT IS '
                           'ON                       ',
                           '     MISC MISC. LABOR OPERATION CODE                  ',
                           '           30461   CP  0.02  1.50   3750   26250                 '
                           '262.50   262.50',
                           '        1 12690512 (S)VALVE         2596    5841     0   58.41    '
                           '58.41    58.41',
                           ' 117781 PERFORMED DIAG P0496 00 1.50 REPLACED EVAP PURGE '
                           'SOLENOID   ',
                           ' '
                           'VALVE                                                                  ',
                           'D** COMPLETE USED CAR '
                           'DETAIL                                           ',
                           '     DETAILC COMPLETE USED CAR DETAIL                 ',
                           '           30811   CP  0.00  3.00   6000   24995                 '
                           '249.95   249.95',
                           'E** FIELDS EXPRESS SERVICE,DEXOS CHANGE ENGINE OIL AND FILTER '
                           ',CORRECT ',
                           '        ALL FLUID LEVELS AS REQUIRED,RESET MAINTENANCE INDICATOR '
                           ', TEST',
                           '        DRIVE AS '
                           'APPLICABLE                                            ',
                           '     LOF6 FIELDS EXPRESS SERVICE,DEXOS CHANGE ENGINE  ',
                           '          OIL AND FILTER ,CORRECT ALL FLUID LEVELS AS ',
                           '          REQUIRED,RESET MAINTENANCE INDICATOR , TEST ',
                           '          DRIVE AS APPLICABLE                         ',
                           '           30461   CM  0.01  0.40   1000    2740                  '
                           '27.40    27.40',
                           '        1 12707246 (S)FILTER         496     993     0    '
                           '9.93     9.93     9.93',
                           '        6 19432354 OIL              2676    5352     0    '
                           '8.92     8.92    53.52  214048                         CUSTOMER '
                           '#: '
                           '9043650823                                                        '
                           '                                               ',
                           '        1 12616850 (S)SEAL           231     970     0    '
                           '9.70     9.70     9.70',
                           ' 117781 MAINT 0.40 PERFORM OIL '
                           'CHANGE                               ',
                           'CUSTOMER PAY Shop Supplies FOR RE      0    '
                           '4000                           40.00',
                           'ACCOUNT   SALE     COST       CONTROL    ACCOUNT   SALE     '
                           'COST       CONTROL  ',
                           '46000     103745    17250                46700      70106    '
                           '33514              ',
                           '46300          0        0                46001       2740     '
                           '1000              ',
                           '49100       5352     2676                6104R       4000        '
                           '0            RO',
                           '32400      11157        0                32410       2789        '
                           '0              ',
                           '22500     199889  *******                6704           0  '
                           '*******              ',
                           '      COST, SALE, & COMP TOTALS    54440  185943     0',
                           '                                                                         '
                           '1064.85',
                           '                                                                          '
                           '754.58',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                           '
                           '40.00',
                           '                                                                         '
                           '1859.43',
                           '                                                                            '
                           '0.00',
                           '                                                                          '
                           '139.46',
                           '                                                                         '
                           '1998.89  214048                         CUSTOMER #: '
                           '9043650823                                                                '
                           '                                       ']}

SORTED_ROWS = [['A CUSTOMER STATES VEHICLE IS SITTING LOW IN THE REAR END/CHECK AND     ',
                '        ADVISE                                                         ',
                '     15 STEERING/SUSPENSION                           ',
                '           30461   CP  0.01  3.00   7500   52500                 525.00   '
                '525.00',
                '        1 84355910 (S)COMPRESSOR   29253   59676     0  596.76   596.76   '
                '596.76',
                '        1 13500114 (S)RELAY          938    2626     0   26.26    26.26    '
                '26.26',
                ' 117781 REAR LEVEL RIDE COMPRESSOR HAS INTERNAL FAULT 3.00 REPLACED ',
                ' LEVEL RIDE COMPRESSOR AND RELAY                                        '],
               ['B PERFORM COMPLIMENTARY 27-POINT MULTI - POINT INSPECTION , PIT STOP,  ',
                '        AND CAR WASH TREATMENT.                                        ',
                '     MPVI PERFORM COMPLIMENTARY 27-POINT MULTI - POINT',
                '          INSPECTION , PIT STOP, AND CAR WASH         ',
                '          TREATMENT.                                  ',
                '           30461  ISP  0.02  0.00      0       0                   0.00     '
                '0.00',
                ' 117781 PERFORM MPI                                                 '],
               ['C** CUSTOMER STATES THE CHECK ENGINE LIGHT IS ON                       ',
                '     MISC MISC. LABOR OPERATION CODE                  ',
                '           30461   CP  0.02  1.50   3750   26250                 262.50   '
                '262.50',
                '        1 12690512 (S)VALVE         2596    5841     0   58.41    58.41    '
                '58.41',
                ' 117781 PERFORMED DIAG P0496 00 1.50 REPLACED EVAP PURGE SOLENOID   ',
                ' VALVE                                                                  '],
               ['D** COMPLETE USED CAR DETAIL                                           ',
                '     DETAILC COMPLETE USED CAR DETAIL                 ',
                '           30811   CP  0.00  3.00   6000   24995                 249.95   '
                '249.95'],
               ['E** FIELDS EXPRESS SERVICE,DEXOS CHANGE ENGINE OIL AND FILTER ,CORRECT ',
                '        ALL FLUID LEVELS AS REQUIRED,RESET MAINTENANCE INDICATOR , TEST',
                '        DRIVE AS APPLICABLE                                            ',
                '     LOF6 FIELDS EXPRESS SERVICE,DEXOS CHANGE ENGINE  ',
                '          OIL AND FILTER ,CORRECT ALL FLUID LEVELS AS ',
                '          REQUIRED,RESET MAINTENANCE INDICATOR , TEST ',
                '          DRIVE AS APPLICABLE                         ',
                '           30461   CM  0.01  0.40   1000    2740                  27.40    '
                '27.40',
                '        1 12707246 (S)FILTER         496     993     0    9.93     9.93     '
                '9.93',
                '        6 19432354 OIL              2676    5352     0    8.92     8.92    '
                '53.52  214048                         CUSTOMER #: '
                '9043650823                                                                 '
                '                                      ',
                '        1 12616850 (S)SEAL           231     970     0    9.70     9.70     '
                '9.70',
                ' 117781 MAINT 0.40 PERFORM OIL CHANGE                               ',
                'CUSTOMER PAY Shop Supplies FOR RE      0    4000                           '
                '40.00']]

REPAIR_ORDER = '214048'
PARSED_ITEMS = [
    ExtractData(repair_order_number='214048',
                labor_operation='15',
                labor_type='CP',
                sold_hours='3.00',
                cost='7500',
                sale_amount='525.00'),
    ExtractData(repair_order_number='214048',
                labor_operation='MPVI',
                labor_type='ISP',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='214048',
                labor_operation='MISC',
                labor_type='CP',
                sold_hours='1.50',
                cost='3750',
                sale_amount='262.50'),
    ExtractData(repair_order_number='214048',
                labor_operation='DETAILC',
                labor_type='CP',
                sold_hours='3.00',
                cost='6000',
                sale_amount='249.95'),
    ExtractData(repair_order_number='214048',
                labor_operation='LOF6',
                labor_type='CM',
                sold_hours='0.40',
                cost='1000',
                sale_amount='27.40')
]


def test_read_table():
    pdf_parser = PDFParser(FILEPATH)
    tables, _ = pdf_parser.parse_tables()
    assert tables == PARSED_TABLE
    return tables


def test_sorting_rows():
    tables = test_read_table()
    sorted_rows = LinesParser(tables[REPAIR_ORDER]).sort_table_rows()
    assert sorted_rows == SORTED_ROWS
    return sorted_rows


def test_parse_items():
    sorted_rows = test_sorting_rows()
    items = []
    for row in sorted_rows:
        row_parser = RowParser(REPAIR_ORDER, row)
        for item in row_parser.parse_items():
            items.append(item)

        assert not row_parser.parse_errors

    assert all(item in PARSED_ITEMS for item in items)


def test_table_without_parts_lines():
    test_parse_items()


if __name__ == '__main__':
    test_table_without_parts_lines()
