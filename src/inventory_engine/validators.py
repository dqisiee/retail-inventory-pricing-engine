from typing import Any, Iterable, List
from .models import InventoryRecord

VALID_CATEGORIES = frozenset({"outer wear", "tops", "bottoms", "accessories"})
MIN_BRANCH_LEN = 3
MIN_ITEM_NAME_LEN = 4
MIN_PRICE_CENTS = 100
CASH_ROUNDING_BASE = 5


def is_valid_record(record: Any) -> bool:
    if not isinstance(record, (tuple, list)) or len(record) != 5:
        return False

    branch, item_name, category, price, quantity = record

    if not (isinstance(branch, str) and len(branch) >= MIN_BRANCH_LEN and branch == branch.strip()):
        return False

    if not (isinstance(item_name, str) and len(item_name) >= MIN_ITEM_NAME_LEN and item_name == item_name.strip()):
        return False

    if not (isinstance(category, str) and category.strip().lower() in VALID_CATEGORIES):
        return False

    if not (isinstance(price, int) and price >= MIN_PRICE_CENTS and price % CASH_ROUNDING_BASE == 0):
        return False

    if not (isinstance(quantity, int) and quantity >= 0):
        return False

    return True


def filter_valid_records(raw_inventory: Iterable[Any]) -> List[InventoryRecord]:
    valid_records: List[InventoryRecord] = []
    for row in raw_inventory:
        if is_valid_record(row):
            valid_records.append(
                InventoryRecord(
                    branch=row[0],
                    item_name=row[1],
                    category=row[2].strip().lower(),
                    price_cents=row[3],
                    quantity=row[4],
                )
            )
    return valid_records