from dataclasses import dataclass
from enum import Enum


class StockFlag(str, Enum):
    LOW_STOCK = "LS"
    SELLING_SLOW = "SS"
    HIGH_STOCK = "HS"


@dataclass(frozen=True)
class InventoryRecord:
    branch: str
    item_name: str
    category: str
    price_cents: int
    quantity: int


@dataclass(frozen=True)
class StockAuditRecord:
    branch: str
    status_flag: StockFlag
    item_name: str
    quantity: int


@dataclass(frozen=True)
class PriceDiscrepancyRecord:
    branch: str
    item_name: str
    price_cents: int
    quantity: int


@dataclass(frozen=True)
class DiscountedItemRecord:
    description: str
    original_price_cents: int
    discounted_price_cents: int
    projected_sales_cents: int
    