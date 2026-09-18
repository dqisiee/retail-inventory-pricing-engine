from src.inventory_engine.audit import detect_price_discrepancies
from src.inventory_engine.models import InventoryRecord


def test_detect_price_discrepancies_catches_divergent_prices():
    records = [
        InventoryRecord("Store A", "Leather Belt", "accessories", 2500, 5),
        InventoryRecord("Store B", "Leather Belt", "accessories", 2800, 3),
        InventoryRecord("Store C", "Canvas Bag", "accessories", 1500, 10),
    ]
    results = detect_price_discrepancies(records)
    assert len(results) == 2
    assert all(r.item_name == "Leather Belt" for r in results)


def test_out_of_stock_items_ignored_in_discrepancy():
    records = [
        InventoryRecord("Store A", "Wool Scarf", "accessories", 3000, 0),
        InventoryRecord("Store B", "Wool Scarf", "accessories", 3500, 5),
    ]
    results = detect_price_discrepancies(records)
    assert len(results) == 0