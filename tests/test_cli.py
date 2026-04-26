import os
import json
import pytest
import pandas as pd
from same_same.cli import main
from unittest.mock import patch

def test_cli_full_run(tmp_path):
    # Setup dummy data
    company_csv = tmp_path / "company.csv"
    vendor_csv = tmp_path / "vendor.csv"
    config_json = tmp_path / "config.json"
    report_html = tmp_path / "report.html"
    
    pd.DataFrame({"description": ["Bug A", "Bug B"]}).to_csv(company_csv, index=False)
    pd.DataFrame({"summary": ["Defect A", "Defect C"]}).to_csv(vendor_csv, index=False)
    
    config = {
        "company_csv_path": str(company_csv),
        "vendor_csv_path": str(vendor_csv),
        "company_desc_col": "description",
        "vendor_desc_col": "summary",
        "threshold": 0.5,
        "output_report": str(report_html)
    }
    with open(config_json, "w") as f:
        json.dump(config, f)
        
    # Run CLI
    with patch("sys.argv", ["same-same", "--config", str(config_json)]):
        with patch("builtins.print"):
            main()
            
    # Verify
    assert os.path.exists(report_html)
    with open(report_html, "r") as f:
        content = f.read()
        assert "# same-same Deduplication Report" in content
