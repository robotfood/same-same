# Same-Same

Semantic defect deduplication tool.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
python3 -m spacy download en_core_web_md
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
same-same --config config.json
```
