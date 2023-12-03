import os
from pathlib import Path
from interactors.items import ExtractData
from tests.services import test_parse

FILEPATH = os.path.join(Path(__file__).parent, 'static', '735376.pdf')
PARSED_TABLE = {'735376': ['A FIELDS COURTESY '
                           'INSPECTION                                           ',
                           '     MULTI FIELDS COURTESY INSPECTION                 ',
                           '              99  ISP        0.00      0       '
                           '0                   0.00     0.00',
                           'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE '
                           'A:        0.00',
                           '  --service                       IT IS THE VISION AND TEAM '
                           'MISSION OF ALL     ',
                           '                                  FIELDS EMPLOYEES TO SERVE '
                           'YOU.               ',
                           '                                  AS A COURTESY TO OUR '
                           'CUSTOMERS,WE PROVIDE    ',
                           '                                  VEHICLE WASH, MINOR ROAD TESTS '
                           'AND DRIVE     ',
                           '                                  IN/OUTS WHEN SERVICING YOUR '
                           'VEHICLE.         ',
                           ' ',
                           '                                  THANK YOU FOR YOUR '
                           'BUSINESS.                 ',
                           '*** NO RO PUNCH TIMES ON FILE ***',
                           ' ']}

SORTED_ROWS = [['A FIELDS COURTESY INSPECTION                                           ',
                '     MULTI FIELDS COURTESY INSPECTION                 ',
                '              99  ISP        0.00      0       0                   0.00     '
                '0.00',
                'PARTS:      0.00  LABOR:      0.00  OTHER:      0.00   TOTAL LINE A:        '
                '0.00',
                '  --service                       IT IS THE VISION AND TEAM MISSION OF '
                'ALL     ',
                '                                  FIELDS EMPLOYEES TO SERVE '
                'YOU.               ',
                '                                  AS A COURTESY TO OUR CUSTOMERS,WE '
                'PROVIDE    ',
                '                                  VEHICLE WASH, MINOR ROAD TESTS AND '
                'DRIVE     ',
                '                                  IN/OUTS WHEN SERVICING YOUR '
                'VEHICLE.         ',
                ' ',
                '                                  THANK YOU FOR YOUR '
                'BUSINESS.                 ',
                '*** NO RO PUNCH TIMES ON FILE ***']]

REPAIR_ORDER = '735376'
PARSED_ITEMS = [
    ExtractData(repair_order_number='735376',
                labor_operation='MULTI',
                labor_type='ISP',
                sold_hours='0.00',
                cost='0',
                sale_amount='0.00'
                )
]


def test_single_row():
    test_parse(FILEPATH, REPAIR_ORDER, PARSED_TABLE, SORTED_ROWS, PARSED_ITEMS)


if __name__ == '__main__':
    test_single_row()
