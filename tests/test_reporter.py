from same_same.reporter import Reporter
from typing import List, Dict

def test_generate_report(tmp_path):
    matches = [
        {'score': 0.95, 'company_desc': 'C1', 'vendor_desc': 'V1'},
        {'score': 0.90, 'company_desc': 'C2', 'vendor_desc': 'V2'}
    ]
    output_path = tmp_path / "report.md"
    reporter = Reporter(str(output_path))
    reporter.generate(matches, threshold=0.85)
    
    content = output_path.read_text()
    assert "# same-same Deduplication Report" in content
    assert "| 0.9500 | C1 | V1 |" in content
    assert "| 0.9000 | C2 | V2 |" in content

def test_generate_report_with_special_chars(tmp_path):
    matches = [
        {'score': 0.95, 'company_desc': 'Pipe | in desc', 'vendor_desc': 'Newline\nin desc'}
    ]
    output_path = tmp_path / "report_special.md"
    reporter = Reporter(str(output_path))
    reporter.generate(matches, threshold=0.85)
    
    content = output_path.read_text()
    # Pipes should be escaped, newlines should be replaced
    assert "Pipe \\| in desc" in content
    assert "Newline in desc" in content or "Newline <br> in desc" in content
