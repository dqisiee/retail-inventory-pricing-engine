from src.inventory_engine.audit import detect_price_discrepancies
from src.inventory_engine.pricing import apply_promotional_discounts
from src.inventory_engine.stocktake import run_stocktake
from src.inventory_engine.validators import filter_valid_records

SAMPLE_RAW_INVENTORY = [
    ("CBD Store", "Linen Shirt", "tops", 6000, 15),
    ("North Store", "Linen Shirt", "tops", 6500, 8),
    ("CBD Store", "Denim Jeans", "bottoms", 8000, 2),
    ("Bad Branch ", "Invalid Item", "tops", 50, 10),
    ("South Store", "Rain Jacket", "outer wear", 16000, 100),
]


def main():
    print("1. Ingesting & Validating Records...")
    valid_records = filter_valid_records(SAMPLE_RAW_INVENTORY)
    print(f"-> {len(valid_records)} valid records retained.")

    print("\n2. Evaluating Stocktake Thresholds...")
    flagged_stock = run_stocktake(valid_records)
    print(f"-> {len(flagged_stock)} items flagged for inventory review.")

    print("\n3. Auditing Cross-Branch Price Discrepancies...")
    discrepancies = detect_price_discrepancies(valid_records)
    print(f"-> {len(discrepancies)} instances of price divergence detected.")

    print("\n4. Applying Promotional Discount Matrix...")
    markdowns = apply_promotional_discounts(valid_records)
    print(f"-> {len(markdowns)} items processed for markdowns.")
    for item in markdowns:
        print(f"   [{item.description}] {item.original_price_cents}c -> {item.discounted_price_cents}c")


if __name__ == "__main__":
    main()