import json
from same_same.config import load_config

def test_load_config(tmp_path):
    config_data = {
        "company_csv_path": "company.csv",
        "vendor_csv_path": "vendor.csv",
        "company_desc_col": "Description",
        "vendor_desc_col": "Summary",
        "threshold": 0.85,
        "output_report": "report.md"
    }
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(config_data))
    
    config = load_config(str(config_file))
    assert config["threshold"] == 0.85
    assert config["company_csv_path"] == "company.csv"
