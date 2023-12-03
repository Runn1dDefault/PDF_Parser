import os
from pathlib import Path

from interactors.items import ExtractData
from tests.services import test_parse

FILEPATH = os.path.join(Path(__file__).parent, 'static', 'DSDA ACCOUNTING COPIES ANNE MARIE 100.pdf')
print(FILEPATH)
PARSED_TABLE = {'61510': ['A [CUSTOMER STATES THERE IS A NOISE IN FRONT THINKS IT COULD BE A WHEEL',
                          '        BEARING                                                        ',
                          'CAUSE: F                                                               ',
                          'CONCERN CODE:                                                                        ',
                          '     03500501 Bearings, pinion - Replace All others   ',
                          '            8327  WJE  5.27  3.50  12075   41416                 414.16   414.16',
                          '        1 68393980AA SEAL-DRIVE  ',
                          '        PINION                      2325    3875     0   38.75    38.75    38.75',
                          '        1 68398694AA             ',
                          '        BEARING-DRIVE PINION        6255   10500     0  105.00   105.00   105.00',
                          '        1 68393926AA SPACER-DRIVE',
                          '        PINION BEARING              1025    1710     0   17.10    17.10    17.10',
                          '        1 68400363AA             ',
                          '        BEARING-DRIVE PINION        3830    6385     0   63.85    63.85    63.85',
                          '        2 68391575AA             ',
                          '        BEARING-DIFFERENTIAL SIDE  12540   21000     0  105.00   105.00   210.00',
                          '        1 68393925AA NUT-PINION      550     920     0    9.20     9.20     9.20',
                          '        2 68393973AA SEAL-AXLE   ',
                          '        DRIVE SHAFT                 4020    6700     0   33.50    33.50    67.00',
                          '        2 68499023AA BEARING-AXLE',
                          '        SHAFT                      20200   34000     0  170.00   170.00   340.00',
                          '        2 68499022AA RING-AXLE   ',
                          '        SHAFT                       3430    5720     0   28.60    28.60    57.20',
                          '        1 68218657AB LUBE-AXLE      1606    3003     0   30.03    30.03    30.03',
                          '        1 68393981AA GASKET-REAR ',
                          '        COVER                       2975    4960     0   49.60    49.60    49.60',
                          '     03400809 REPLACE DIFF SIDE BEARINGS              ',
                          '            8327  WJE  0.00  0.50   1725    5917                  59.17    59.17',
                          '     03200506 REPLACE RIGHT REAR AXLEBEARING          ',
                          '            8327  WJE  0.00  0.50   1725    5917                  59.17    59.17',
                          '     03200507 REPLACE AXLE TUBE BEARING               ',
                          '            8327  WJE  0.00  0.50   1725    5917                  59.17    59.17',
                          '                                      58756      98773 TPARTS',
                          '                                      17250      59167 TLABOR  61510                '
                          '          CUSTOMER #: 101076                                                         '
                          '                                                  ',
                          'PARTS:    987.73  LABOR:    591.67  OTHER:      0.00   TOTAL LINE A:     1579.40',
                          ' 35811                                                              ',
                          ' test drove. duplicated. found rear differential pinion bearings    ',
                          ' roaring. removed and replaced rear pinion bearings, carrier bearings,  ',
                          ' and axle bearings and all applicable seals/ gaskets.                   ',
                          ' test drove after repair. all okay after repairs                    ',
                          'B Multi-point inspection (according to maintenance interval)           ',
                          '     9090 Multi-point inspection (according to        ',
                          '          maintenance interval)                       ',
                          '            8327  CJM  0.00  0.00      0       0                   0.00     0.00',
                          'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE B:        0.00',
                          '  GAVE TO CHAD 10-5                                                            ',
                          '    DATE   START  FINISH  DURATION  TYPE  TECH    LINE(S)  CHG',
                          '10-04-22   09:51   10:47      0.93     W    8327        A    ',
                          '10-06-22   10:14   14:34      4.34     W    8327        A    ',
                          'ACCOUNT   SALE     COST       CONTROL    ACCOUNT   SALE     COST       CONTROL  ',
                          '55200      59167    17250                57200      98773    58756              ',
                          '55000          0        0                11600     157940  *******              ',
                          '11700          0  *******                ',
                          '      COST, SALE, & COMP TOTALS    76006  157940     0',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00',
                          '                                                                            0.00  61510 '
                          '                         CUSTOMER #: 101076                                             '
                          '                                                              ']}

SORTED_ROWS = [['A [CUSTOMER STATES THERE IS A NOISE IN FRONT THINKS IT COULD BE A WHEEL',
                '        BEARING                                                        ',
                'CAUSE: F                                                               ',
                'CONCERN '
                'CODE:                                                                        ',
                '     03500501 Bearings, pinion - Replace All others   ',
                '            8327  WJE  5.27  3.50  12075   41416                 414.16   '
                '414.16',
                '        1 68393980AA SEAL-DRIVE  ',
                '        PINION                      2325    3875     0   38.75    38.75    '
                '38.75',
                '        1 68398694AA             ',
                '        BEARING-DRIVE PINION        6255   10500     0  105.00   105.00   '
                '105.00',
                '        1 68393926AA SPACER-DRIVE',
                '        PINION BEARING              1025    1710     0   17.10    17.10    '
                '17.10',
                '        1 68400363AA             ',
                '        BEARING-DRIVE PINION        3830    6385     0   63.85    63.85    '
                '63.85',
                '        2 68391575AA             ',
                '        BEARING-DIFFERENTIAL SIDE  12540   21000     0  105.00   105.00   '
                '210.00',
                '        1 68393925AA NUT-PINION      550     920     0    9.20     9.20     '
                '9.20',
                '        2 68393973AA SEAL-AXLE   ',
                '        DRIVE SHAFT                 4020    6700     0   33.50    33.50    '
                '67.00',
                '        2 68499023AA BEARING-AXLE',
                '        SHAFT                      20200   34000     0  170.00   170.00   '
                '340.00',
                '        2 68499022AA RING-AXLE   ',
                '        SHAFT                       3430    5720     0   28.60    28.60    '
                '57.20',
                '        1 68218657AB LUBE-AXLE      1606    3003     0   30.03    30.03    '
                '30.03',
                '        1 68393981AA GASKET-REAR ',
                '        COVER                       2975    4960     0   49.60    49.60    '
                '49.60',
                '     03400809 REPLACE DIFF SIDE BEARINGS              ',
                '            8327  WJE  0.00  0.50   1725    5917                  59.17    '
                '59.17',
                '     03200506 REPLACE RIGHT REAR AXLEBEARING          ',
                '            8327  WJE  0.00  0.50   1725    5917                  59.17    '
                '59.17',
                '     03200507 REPLACE AXLE TUBE BEARING               ',
                '            8327  WJE  0.00  0.50   1725    5917                  59.17    '
                '59.17',
                '                                      58756      98773 TPARTS',
                '                                      17250      59167 TLABOR  '
                '61510                          CUSTOMER #: '
                '101076                                                                   '
                '                                        ',
                'PARTS:    987.73  LABOR:    591.67  OTHER:      0.00   TOTAL LINE A:     '
                '1579.40',
                ' 35811                                                              ',
                ' test drove. duplicated. found rear differential pinion bearings    ',
                ' roaring. removed and replaced rear pinion bearings, carrier bearings,  ',
                ' and axle bearings and all applicable seals/ gaskets.                   ',
                ' test drove after repair. all okay after repairs                    '],
               ['B Multi-point inspection (according to maintenance interval)           ',
                '     9090 Multi-point inspection (according to        ',
                '          maintenance interval)                       ',
                '            8327  CJM  0.00  0.00      0       0                   0.00     '
                '0.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE B:        '
                '0.00',
                '  GAVE TO CHAD '
                '10-5                                                            ',
                '    DATE   START  FINISH  DURATION  TYPE  TECH    LINE(S)  CHG',
                '10-04-22   09:51   10:47      0.93     W    8327        A    ',
                '10-06-22   10:14   14:34      4.34     W    8327        A    ']]

REPAIR_ORDER = '61510'
PARSED_ITEMS = [
    ExtractData(repair_order_number=REPAIR_ORDER, labor_operation='03500501', labor_type='WJE', sold_hours='3.50',
                cost='12075', sale_amount='414.16'),
    ExtractData(repair_order_number=REPAIR_ORDER, labor_operation='03400809', labor_type='WJE', sold_hours='0.50',
                cost='1725', sale_amount='59.17'),
    ExtractData(repair_order_number=REPAIR_ORDER, labor_operation='03200506', labor_type='WJE', sold_hours='0.50',
                cost='1725', sale_amount='59.17'),
    ExtractData(repair_order_number=REPAIR_ORDER, labor_operation='03200507', labor_type='WJE', sold_hours='0.50',
                cost='1725', sale_amount='59.17'),
    ExtractData(repair_order_number=REPAIR_ORDER, labor_operation='9090', labor_type='CJM', sold_hours='0.00',
                cost='0', sale_amount='0.00')
]


def test_multiple_items_from_one_row():
    test_parse(FILEPATH, REPAIR_ORDER, PARSED_TABLE, SORTED_ROWS, PARSED_ITEMS)


if __name__ == '__main__':
    test_multiple_items_from_one_row()
