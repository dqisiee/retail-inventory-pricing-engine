from typing import Dict, List, Optional, Tuple
from .models import DiscountedItemRecord, InventoryRecord

DEFAULT_DISCOUNT_RATE = 0.20
CASH_ROUNDING_BASE = 5

CATEGORY_DISCOUNT_TIERS: Dict[str, Tuple[int, Optional[int], float]] = {
    "outer wear": (15000, None, 0.70),
    "tops": (5000, 9000, 0.60),
    "bottoms": (5000, 15000, 0.40),
    "accessories": (1000, 5000, 0.45),
}


def calculate_discount_rate(category: str, price_cents: int) -> float:
    tier = CATEGORY_DISCOUNT_TIERS.get(category)
    if not tier:
        return DEFAULT_DISCOUNT_RATE

    min_price, max_price, tier_rate = tier
    if max_price is None:
        if price_cents >= min_price:
            return tier_rate
    elif min_price <= price_cents <= max_price:
        return tier_rate

    return DEFAULT_DISCOUNT_RATE


def apply_promotional_discounts(inventory: List[InventoryRecord]) -> List[DiscountedItemRecord]:
    discounted_items: List[DiscountedItemRecord] = []

    for item in inventory:
        if item.quantity <= 0 or item.price_cents < 100:
            continue

        rate = calculate_discount_rate(item.category, item.price_cents)
        computed_price = item.price_cents * (1.0 - rate)
        rounded_price = int(computed_price - (computed_price % CASH_ROUNDING_BASE))
        projected_sales = rounded_price * item.quantity

        description = f"{item.branch}: {item.item_name} ({item.category})"
        discounted_items.append(
            DiscountedItemRecord(
                description=description,
                original_price_cents=item.price_cents,
                discounted_price_cents=rounded_price,
                projected_sales_cents=projected_sales,
            )
        )

    return discounted_items