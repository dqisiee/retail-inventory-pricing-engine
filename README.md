# Retail Inventory & Pricing Audit Engine

An automated Python data validation and audit pipeline designed to sanitise retail stock records, detect cross-branch pricing inconsistencies, evaluate stock velocity, and execute dynamic promotional markdowns.

---

## Key Features

- **Data Ingestion & Validation:** Sanitises raw, unvalidated inventory records against strict domain constraints (non-empty naming, valid catalog departments, non-negative quantities, cash-rounding compatibility).
- **Stocktake Health Profiling:** Automatically tags items exceeding or falling below inventory thresholds (`LS` for Low Stock, `SS` for Selling Slow, `HS` for High Stock).
- **Multi-Branch Pricing Anomaly Detection:** Identifies SKU-level pricing divergences across regional store locations to protect retail margins.
- **Dynamic Markdown Engine:** Applies tiered category discounting matrices, models promotional price elasticity, and calculates projected sales with cash-rounding logic.
- **Strict Typing & Domain Models:** Built with immutable `@dataclass` models and enums for type safety and maintainability.

---

## Project Structure

```text
├── src/
│   └── inventory_engine/
│       ├── __init__.py
│       ├── models.py         # Dataclasses and Enums
│       ├── validators.py     # Input record sanitization
│       ├── stocktake.py      # Threshold and velocity audits
│       ├── audit.py          # Cross-branch discrepancy detection
│       └── pricing.py        # Markdown calculation engine
├── tests/
│   ├── __init__.py
│   └── test_audit.py         # Automated pytest test suite
├── main.py                   # Pipeline entrypoint
├── requirements.txt          # Dependencies
└── README.md
