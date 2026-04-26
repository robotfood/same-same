from same_same.reporter import Reporter
import os

def test_generate_report_with_pipes(tmp_path):
    matches = [
        {'score': 0.95, 'company_desc': 'Description with | pipe', 'vendor_desc': 'Vendor | pipe'}
    ]
    output_path = tmp_path / "robust_report.md"
    reporter = Reporter(str(output_path))
    reporter.generate(matches, threshold=0.85)
    
    content = output_path.read_text()
    # If pipes aren't escaped, this will have more than 4 pipes in the row line
    # Standard row: | score | company | vendor | -> 4 pipes
    row_line = [line for line in content.split('\n') if '0.9500' in line][0]
    pipe_count = row_line.count('|')
    print(f"Row line: {row_line}")
    print(f"Pipe count: {pipe_count}")
    assert pipe_count == 4, f"Expected 4 pipes, found {pipe_count}. Pipes in descriptions must be escaped."

