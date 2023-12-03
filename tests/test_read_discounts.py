import os
from pathlib import Path

from interactors.items import ExtractData
from tests.services import test_parse

FILEPATH = os.path.join(Path(__file__).parent, 'static', '514891-discounts.pdf')
PARSED_TABLE = {'514891': ['A PERFORMED USED CAR INSPECTION-WRITE BRAKE PAD THICKNESS ON '
                           'INSPECTION',
                           '        '
                           'SHEET                                                          ',
                           '     USED PERFORMED USED CAR INSPECTION-WRITE BRAKE   ',
                           '          PAD THICKNESS ON INSPECTION SHEET           ',
                           '              17  IUC  0.84  1.00   4120   19900                 '
                           '199.00   199.00',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          LABOR   IUC                  0   -3980                 '
                           '-39.80   -39.80',
                           'PARTS:      0.00  LABOR:    199.00  OTHER:    -39.80   TOTAL LINE '
                           'A:      159.20',
                           ' 78538 1.00 PERFORM USED CAR '
                           'INSPECTION                             ',
                           'B INSERT FIELDS LICENSE PLATE '
                           'INSERTS                                  ',
                           '     62 INSERT LICENSE PLATE INSERTS                  ',
                           '              99  IUC  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           '        4 SS018 SCREW 79855 5X10     100     260     0    '
                           '0.65     0.65     2.60',
                           '        1 SS013 W/W SOLVT 20     ',
                           '        BELOW                        225     370     0    '
                           '3.70     3.70     3.70',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          PARTS   IUC                  0    -126                  '
                           '-1.26    -1.26',
                           'PARTS:      6.30  LABOR:      0.00  OTHER:     -1.26   TOTAL LINE '
                           'B:        5.04',
                           'C DELETE STORED NAVIGATION AND PHONE CONTACTS FROM PREVIOUS OWNER '
                           '(IF  ',
                           '        '
                           'EQUIPPED)                                                      ',
                           '     NAV DELETE STORED NAVIGATION AND PHONE CONTACTS  ',
                           '          FROM PREVIOUS OWNER (IF EQUIPPED)           ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE '
                           'C:        0.00',
                           'D PARK CAR OUTSIDE SERVICE ENTRACE AND GIVE KEYS TO '
                           'ADVISOR            ',
                           '     DONE PARK CAR OUTSIDE SERVICE ENTRACE AND GIVE   ',
                           '          KEYS TO ADVISOR                             ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE '
                           'D:        0.00',
                           'E OIL CHANGE COMPLETED ON 09/08/21 AT 72,986 '
                           'MILES                     ',
                           '     I INFORMATION                                    ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE '
                           'E:        0.00',
                           'F PERFORM PAINTLESS DENT '
                           'REMOVAL                                         '
                           '514891                         CUSTOMER #: '
                           '700                                                                '
                           '                                              ',
                           '     DW PERFORM PAINTLESS DENT REMOVAL                ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'SUBL DENT WIZARD PO '
                           '62573                                              ',
                           '                  IUC              10000   11000                 '
                           '110.00   110.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:    110.00   TOTAL LINE '
                           'F:      110.00',
                           'G PERFORMED INTERIOR AND EXTERIOR '
                           'DETAIL                               ',
                           '     DETAIL PERFORMED INTERIOR AND EXTERIOR DETAIL    ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'SUBL MOBILE CLICK WASH PO '
                           '62779                                        ',
                           '                  IUC              14000   15400                 '
                           '154.00   154.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:    154.00   TOTAL LINE '
                           'G:      154.00',
                           'H** REPLACE ALL '
                           'WIPERS                                                 ',
                           '     62 REPLACE ALL WIPERS                            ',
                           '              17  IUC  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           '        1 61-61-0-039-697 SET OF ',
                           '        WIPER BLADES:618010         3683    6577     0   65.77    '
                           '65.77    65.77',
                           '        1 61-62-7-294-429 WIPER  ',
                           '        BLADE:618021                 719    1198     0   11.98    '
                           '11.98    11.98',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          PARTS   IUC                  0   -1555                 '
                           '-15.55   -15.55',
                           'PARTS:     77.75  LABOR:      0.00  OTHER:    -15.55   TOTAL LINE '
                           'H:       62.20',
                           ' 78538 REPLACE STREAKING FRONT AND REAR WIPER '
                           'BLADES                ',
                           'I** DURING INSPECTION FOUND NOISE UNDER CENTER CONSOLE. REMOVE '
                           'LOOSE   ',
                           '        ITEMS FROM UNDER THE CENTER '
                           'CONSOLE.                           ',
                           '     62 I                                             ',
                           '              17  IUC  2.51  3.00  12360   59700                 '
                           '597.00   597.00',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          LABOR   IUC                  0  -11940                '
                           '-119.40  -119.40',
                           'PARTS:      0.00  LABOR:    597.00  OTHER:   -119.40   TOTAL LINE '
                           'I:      477.60',
                           ' 78538 3.00 LOCATE ROLLING NOISE AND REMOVE COIN FROM UNDER '
                           'CENTER  ',
                           ' CONSOLE '
                           'ASSEMBLY                                                       ',
                           'J** DURING INSPECTION FOUND REAR HATCH RATTLE. INSPECT REAR '
                           'RATTLE.    ',
                           '     62 INSULATE REAR HATCH                           ',
                           '              17  IUC  1.81  1.00   4120   19900                 '
                           '199.00   199.00  514891                         CUSTOMER #: '
                           '700                                                                '
                           '                                              ',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          LABOR   IUC                  0   -3980                 '
                           '-39.80   -39.80',
                           'PARTS:      0.00  LABOR:    199.00  OTHER:    -39.80   TOTAL LINE '
                           'J:      159.20',
                           ' 78538 1.00 LOCATE AND ELIMINATE RATTLE FROM REAR '
                           'HATCH.            ',
                           'K** REPLACE MISSING LIFTING '
                           'PAD                                        ',
                           '     62 REPLACE LIFTING PAD                           ',
                           '              17  IUC  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           '        1 51-71-7-189-259 SUPPORT',
                           '        LIFTING PLATFORM:517170     1753    2922     0   29.22    '
                           '29.22    29.22',
                           'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS '
                           'OLD                        ',
                           '          PARTS   IUC                  0    -584                  '
                           '-5.84    -5.84',
                           'PARTS:     29.22  LABOR:      0.00  OTHER:     -5.84   TOTAL LINE '
                           'K:       23.38',
                           ' 78538 INSTALL MISSING RIGHT REAR LIFTING '
                           'PAD                       ',
                           'L** NORTHSHORE NOVUS WINDSHIELD '
                           'REPAIR                                 ',
                           '     I NOVUS WINDSHIELD REPAIR                        ',
                           '              99    I  0.00  0.00      0       '
                           '0                   0.00     0.00',
                           'SUBL NOVUS WINDSHIELD PO '
                           '62712                                         ',
                           '                  IUC              10500   11550                 '
                           '115.50   115.50',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:    115.50   TOTAL LINE '
                           'L:      115.50',
                           '                                  THANK YOU FOR VISITING FIELDS '
                           'BMW. AS A      ',
                           '                                  COURTESY TO OUR CUSTOMERS, WE '
                           'PROVIDE VEHICLE',
                           '                                  WASH, MINOR ROAD TESTS AND '
                           'DRIVE IN/OUTS WHEN',
                           '                                  SERVICING YOUR '
                           'VEHICLE.                      ',
                           '    DATE   START  FINISH  DURATION  TYPE  TECH    LINE(S)  CHG',
                           '12-03-21   07:41   08:31      0.84     W      17        A    ',
                           '12-06-21   07:45   08:37      0.87     W      17        I    ',
                           '           09:48   09:48      0.00     W      17        H    ',
                           '           09:48   10:29      0.68     W      17        I    ',
                           '           14:26   15:02      0.60     W      17        I    ',
                           '12-07-21   08:12   08:33      0.35     W      17        I    ',
                           '           09:10   09:19      0.15     W      17        J    ',
                           '           10:21   10:37      0.27     W      17        J    ',
                           '           11:47   13:10      1.39     W      17        J      '
                           '514891                         CUSTOMER #: '
                           '700                                                           '
                           '                                                   ',
                           '           13:10   13:11      0.01     W      17        I    ',
                           '           13:11   13:11      0.00     W      17        K    ',
                           'ACCOUNT   SALE     COST       CONTROL    ACCOUNT   SALE     '
                           'COST       CONTROL  ',
                           '4551       99500    20600                0162      -22165        '
                           '0              ',
                           '4651       11327     6480                4562       37950    '
                           '34500              ',
                           '2401      126612  *******                0683           0  '
                           '*******              ',
                           '      COST, SALE, & COMP TOTALS    61580  126612     0',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00',
                           '                                                                            '
                           '0.00  514891                         CUSTOMER #: '
                           '700                                                                         '
                           '                                     ']}

SORTED_ROWS = [['A PERFORMED USED CAR INSPECTION-WRITE BRAKE PAD THICKNESS ON INSPECTION',
                '        SHEET                                                          ',
                '     USED PERFORMED USED CAR INSPECTION-WRITE BRAKE   ',
                '          PAD THICKNESS ON INSPECTION SHEET           ',
                '              17  IUC  0.84  1.00   4120   19900                 199.00   '
                '199.00',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          LABOR   IUC                  0   -3980                 -39.80   '
                '-39.80',
                'PARTS:      0.00  LABOR:    199.00  OTHER:    -39.80   TOTAL LINE A:      '
                '159.20',
                ' 78538 1.00 PERFORM USED CAR INSPECTION                             '],
               ['B INSERT FIELDS LICENSE PLATE INSERTS                                  ',
                '     62 INSERT LICENSE PLATE INSERTS                  ',
                '              99  IUC  0.00  0.00      0       0                   0.00     '
                '0.00',
                '        4 SS018 SCREW 79855 5X10     100     260     0    0.65     0.65     '
                '2.60',
                '        1 SS013 W/W SOLVT 20     ',
                '        BELOW                        225     370     0    3.70     3.70     '
                '3.70',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          PARTS   IUC                  0    -126                  -1.26    '
                '-1.26',
                'PARTS:      6.30  LABOR:      0.00  OTHER:     -1.26   TOTAL LINE B:        '
                '5.04'],
               ['C DELETE STORED NAVIGATION AND PHONE CONTACTS FROM PREVIOUS OWNER (IF  ',
                '        EQUIPPED)                                                      ',
                '     NAV DELETE STORED NAVIGATION AND PHONE CONTACTS  ',
                '          FROM PREVIOUS OWNER (IF EQUIPPED)           ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE C:        '
                '0.00'],
               ['D PARK CAR OUTSIDE SERVICE ENTRACE AND GIVE KEYS TO ADVISOR            ',
                '     DONE PARK CAR OUTSIDE SERVICE ENTRACE AND GIVE   ',
                '          KEYS TO ADVISOR                             ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE D:        '
                '0.00'],
               ['E OIL CHANGE COMPLETED ON 09/08/21 AT 72,986 MILES                     ',
                '     I INFORMATION                                    ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE E:        '
                '0.00'],
               ['F PERFORM PAINTLESS DENT REMOVAL                                         '
                '514891                         CUSTOMER #: '
                '700                                                                        '
                '                                      ',
                '     DW PERFORM PAINTLESS DENT REMOVAL                ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'SUBL DENT WIZARD PO 62573                                              ',
                '                  IUC              10000   11000                 110.00   '
                '110.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:    110.00   TOTAL LINE F:      '
                '110.00'],
               ['G PERFORMED INTERIOR AND EXTERIOR DETAIL                               ',
                '     DETAIL PERFORMED INTERIOR AND EXTERIOR DETAIL    ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'SUBL MOBILE CLICK WASH PO 62779                                        ',
                '                  IUC              14000   15400                 154.00   '
                '154.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:    154.00   TOTAL LINE G:      '
                '154.00'],
               ['H** REPLACE ALL WIPERS                                                 ',
                '     62 REPLACE ALL WIPERS                            ',
                '              17  IUC  0.00  0.00      0       0                   0.00     '
                '0.00',
                '        1 61-61-0-039-697 SET OF ',
                '        WIPER BLADES:618010         3683    6577     0   65.77    65.77    '
                '65.77',
                '        1 61-62-7-294-429 WIPER  ',
                '        BLADE:618021                 719    1198     0   11.98    11.98    '
                '11.98',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          PARTS   IUC                  0   -1555                 -15.55   '
                '-15.55',
                'PARTS:     77.75  LABOR:      0.00  OTHER:    -15.55   TOTAL LINE H:       '
                '62.20',
                ' 78538 REPLACE STREAKING FRONT AND REAR WIPER BLADES                '],
               ['I** DURING INSPECTION FOUND NOISE UNDER CENTER CONSOLE. REMOVE LOOSE   ',
                '        ITEMS FROM UNDER THE CENTER CONSOLE.                           ',
                '     62 I                                             ',
                '              17  IUC  2.51  3.00  12360   59700                 597.00   '
                '597.00',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          LABOR   IUC                  0  -11940                -119.40  '
                '-119.40',
                'PARTS:      0.00  LABOR:    597.00  OTHER:   -119.40   TOTAL LINE I:      '
                '477.60',
                ' 78538 3.00 LOCATE ROLLING NOISE AND REMOVE COIN FROM UNDER CENTER  ',
                ' CONSOLE ASSEMBLY                                                       '],
               ['J** DURING INSPECTION FOUND REAR HATCH RATTLE. INSPECT REAR RATTLE.    ',
                '     62 INSULATE REAR HATCH                           ',
                '              17  IUC  1.81  1.00   4120   19900                 199.00   '
                '199.00  514891                         CUSTOMER #: '
                '700                                                                       '
                '                                       ',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          LABOR   IUC                  0   -3980                 -39.80   '
                '-39.80',
                'PARTS:      0.00  LABOR:    199.00  OTHER:    -39.80   TOTAL LINE J:      '
                '159.20',
                ' 78538 1.00 LOCATE AND ELIMINATE RATTLE FROM REAR HATCH.            '],
               ['K** REPLACE MISSING LIFTING PAD                                        ',
                '     62 REPLACE LIFTING PAD                           ',
                '              17  IUC  0.00  0.00      0       0                   0.00     '
                '0.00',
                '        1 51-71-7-189-259 SUPPORT',
                '        LIFTING PLATFORM:517170     1753    2922     0   29.22    29.22    '
                '29.22',
                'UC20 20% DISCOUNT TO USED CARS OVER 5 YEARS OLD                        ',
                '          PARTS   IUC                  0    -584                  -5.84    '
                '-5.84',
                'PARTS:     29.22  LABOR:      0.00  OTHER:     -5.84   TOTAL LINE K:       '
                '23.38',
                ' 78538 INSTALL MISSING RIGHT REAR LIFTING PAD                       '],
               ['L** NORTHSHORE NOVUS WINDSHIELD REPAIR                                 ',
                '     I NOVUS WINDSHIELD REPAIR                        ',
                '              99    I  0.00  0.00      0       0                   0.00     '
                '0.00',
                'SUBL NOVUS WINDSHIELD PO 62712                                         ',
                '                  IUC              10500   11550                 115.50   '
                '115.50',
                'PARTS:      0.00  LABOR:      0.00  OTHER:    115.50   TOTAL LINE L:      '
                '115.50',
                '                                  THANK YOU FOR VISITING FIELDS BMW. AS '
                'A      ',
                '                                  COURTESY TO OUR CUSTOMERS, WE PROVIDE '
                'VEHICLE',
                '                                  WASH, MINOR ROAD TESTS AND DRIVE IN/OUTS '
                'WHEN',
                '                                  SERVICING YOUR '
                'VEHICLE.                      ',
                '    DATE   START  FINISH  DURATION  TYPE  TECH    LINE(S)  CHG',
                '12-03-21   07:41   08:31      0.84     W      17        A    ',
                '12-06-21   07:45   08:37      0.87     W      17        I    ',
                '           09:48   09:48      0.00     W      17        H    ',
                '           09:48   10:29      0.68     W      17        I    ',
                '           14:26   15:02      0.60     W      17        I    ',
                '12-07-21   08:12   08:33      0.35     W      17        I    ',
                '           09:10   09:19      0.15     W      17        J    ',
                '           10:21   10:37      0.27     W      17        J    ',
                '           11:47   13:10      1.39     W      17        J      '
                '514891                         CUSTOMER #: '
                '700                                                             '
                '                                                 ',
                '           13:10   13:11      0.01     W      17        I    ',
                '           13:11   13:11      0.00     W      17        K    ']]

REPAIR_ORDER = '514891'
PARSED_ITEMS = [
    ExtractData(repair_order_number='514891',
                labor_operation='USED',
                labor_type='IUC',
                sold_hours='1.00',
                cost='4120',
                sale_amount='199.00',
                discount='-39.80'),
    ExtractData(repair_order_number='514891',
                labor_operation='62',
                labor_type='IUC',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='NAV',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='DONE',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='I',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='DW',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='DETAIL',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='62',
                labor_type='IUC',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='62',
                labor_type='IUC',
                sold_hours='3.00',
                cost='12360',
                sale_amount='597.00',
                discount='-119.40'),
    ExtractData(repair_order_number='514891',
                labor_operation='62',
                labor_type='IUC',
                sold_hours='1.00',
                cost='4120',
                sale_amount='199.00',
                discount='-39.80'),
    ExtractData(repair_order_number='514891',
                labor_operation='62',
                labor_type='IUC',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'),
    ExtractData(repair_order_number='514891',
                labor_operation='I',
                labor_type='I',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00')
]


def test_discounts():
    test_parse(
        filepath=FILEPATH,
        repair_order=REPAIR_ORDER,
        parsed_table=PARSED_TABLE,
        sorted_rows=SORTED_ROWS,
        parsed_items=PARSED_ITEMS
    )


if __name__ == '__main__':
    test_discounts()
