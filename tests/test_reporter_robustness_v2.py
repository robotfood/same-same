from same_same.reporter import Reporter
import os

def test_generate_report_with_newlines(tmp_path):
    matches = [
        {'score': 0.95, 'company_desc': 'Description with\nnewline', 'vendor_desc': 'Vendor desc'}
    ]
    output_path = tmp_path / "robust_report_v2.md"
    reporter = Reporter(str(output_path))
    reporter.generate(matches, threshold=0.85)
    
    content = output_path.read_text()
    # A newline in a description will create a new line in the file, 
    # which will NOT start with | and thus break the table.
    lines = content.split('\n')
    # Find the row line
    row_idx = -1
    for i, line in enumerate(lines):
        if '0.9500' in line:
            row_idx = i
            break
    
    assert row_idx != -1
    # The next line should NOT be "newline | Vendor desc |"
    # It should ideally be part of the same cell (using <br> or similar) or just escaped.
    print(f"Row: {lines[row_idx]}")
    if row_idx + 1 < len(lines):
        print(f"Next line: {lines[row_idx+1]}")
    
    # If the next line doesn't start with |, the table is broken
    if row_idx + 1 < len(lines) and lines[row_idx+1].strip() and not lines[row_idx+1].strip().startswith('|'):
         assert False, f"Newline in description broke the table. Next line: {lines[row_idx+1]}"

