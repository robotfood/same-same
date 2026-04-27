# Same-Same

Semantic defect deduplication tool.

## Installation

```bash
uv sync --group dev
```

## Usage

Create a `config.json` file:

```json
{
  "company_csv_path": "company_defects.csv",
  "vendor_csv_path": "vendor_defects.csv",
  "company_desc_col": "Description",
  "vendor_desc_col": "Summary",
  "threshold": 0.85,
  "output_report": "deduplication_report.md"
}
```

Then run the tool:

```bash
uv run same-same --config config.json
```

## Testing with Mock Data

You can generate a realistic set of cloud microservices defects (50 internal, 150 vendor) to test the semantic matching:

```bash
# Generate the mock CSV files
uv run python scripts/generate_mock_data.py

# Run deduplication using the mock configuration
uv run same-same --config mock_config.json
```

This will produce `mock_deduplication_report.md` in your project root.
