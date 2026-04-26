from typing import List, Dict

class Reporter:
    """A class to generate Markdown reports for deduplication results."""
    
    def __init__(self, output_path: str):
        """Initialize the reporter with an output path."""
        self.output_path = output_path
    
    def generate(self, matches: List[Dict], threshold: float) -> None:
        """
        Generate a Markdown report listing matches.
        """
        lines = [
            "# same-same Deduplication Report",
            f"\n- **Threshold:** {threshold}",
            f"- **Total Matches:** {len(matches)}",
            "\n| Score | Company Description | Vendor Description |",
            "| :--- | :--- | :--- |"
        ]
        for m in matches:
            # Escape pipes using HTML entity and replace newlines to maintain Markdown table structure
            c_desc = str(m['company_desc']).replace('|', '&#124;').replace('\n', ' ')
            v_desc = str(m['vendor_desc']).replace('|', '&#124;').replace('\n', ' ')
            lines.append(f"| {m['score']:.4f} | {c_desc} | {v_desc} |")
        
        with open(self.output_path, 'w') as f:
            f.write("\n".join(lines))
