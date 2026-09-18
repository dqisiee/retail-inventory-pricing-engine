from typing import Dict, List, Optional, Tuple
from .models import InventoryRecord, StockAuditRecord, StockFlag

STOCKTAKE_THRESHOLDS: Dict[str, Tuple[int, int, int, int]] = {
    "outer wear": (150, 1250, 2000, 3500),
    "tops": (500, 1500, 2000, 3000),
    "bottoms": (300, 1400, 1750, 2500),
    "accessories": (2000, 3500, 5000, 6000),
}


def evaluate_stock_status(category: str, quantity: int) -> Optional[StockFlag]:
    thresholds = STOCKTAKE_THRESHOLDS.get(category)
    if not thresholds:
        return None

    ls_max, ss_min, ss_max, hs_min = thresholds

    if 1 <= quantity <= ls_max:
        return StockFlag.LOW_STOCK
    if ss_min <= quantity <= ss_max:
        return StockFlag.SELLING_SLOW
    if quantity >= hs_min:
        return StockFlag.HIGH_STOCK

    return None


def run_stocktake(inventory: List[InventoryRecord]) -> List[StockAuditRecord]:
    flagged: List[StockAuditRecord] = []
    for item in inventory:
        flag = evaluate_stock_status(item.category, item.quantity)
        if flag:
            flagged.append(
                StockAuditRecord(
                    branch=item.branch,
                    status_flag=flag,
                    item_name=item.item_name,
                    quantity=item.quantity,
                )
            )
    return flagged