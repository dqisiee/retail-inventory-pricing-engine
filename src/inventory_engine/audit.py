from collections import defaultdict
from typing import Dict, List, Set
from .models import InventoryRecord, PriceDiscrepancyRecord


def detect_price_discrepancies(inventory: List[InventoryRecord]) -> List[PriceDiscrepancyRecord]:
    prices_by_item: Dict[str, Set[int]] = defaultdict(set)

    for item in inventory:
        if item.quantity > 0:
            prices_by_item[item.item_name].add(item.price_cents)

    discrepant_items = {
        item_name for item_name, prices in prices_by_item.items() if len(prices) > 1
    }

    results: List[PriceDiscrepancyRecord] = []
    for item in inventory:
        if item.quantity > 0 and item.item_name in discrepant_items:
            results.append(
                PriceDiscrepancyRecord(
                    branch=item.branch,
                    item_name=item.item_name,
                    price_cents=item.price_cents,
                    quantity=item.quantity,
                )
            )
    return results