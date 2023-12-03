from dataclasses import dataclass, asdict


@dataclass
class ExtractData:
    repair_order_number: str
    labor_operation: str = None
    labor_type: str = None
    sold_hours: str = None
    cost: str = None
    sale_amount: str = None
    discount: str = None

    dict = asdict
