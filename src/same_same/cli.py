import sys
import argparse
import pandas as pd
from same_same.config import load_config
from same_same.data_loader import load_data
from same_same.vectorizer import Vectorizer
from same_same.matcher import Matcher
from same_same.reporter import Reporter

def main():
    parser = argparse.ArgumentParser(description="same-same: Semantic defect deduplication")
    parser.add_argument("--config", default="config.json", help="Path to config.json")
    args = parser.parse_args()
    
    try:
        config = load_config(args.config)
        print(f"Loading data...")
        df_company = load_data(config['company_csv_path'])
        df_vendor = load_data(config['vendor_csv_path'])
        
        print("Vectorizing descriptions...")
        vectorizer = Vectorizer()
        company_vecs = vectorizer.vectorize(df_company[config['company_desc_col']].tolist())
        vendor_vecs = vectorizer.vectorize(df_vendor[config['vendor_desc_col']].tolist())
        
        print("Computing similarity...")
        matcher = Matcher(threshold=config['threshold'])
        matches = matcher.find_matches(company_vecs, vendor_vecs)
        
        # Enrich matches with text
        enriched_matches = []
        for m in matches:
            enriched_matches.append({
                'score': m['score'],
                'company_desc': df_company.iloc[m['company_idx']][config['company_desc_col']],
                'vendor_desc': df_vendor.iloc[m['vendor_idx']][config['vendor_desc_col']]
            })
            
        print(f"Generating report: {config['output_report']}")
        reporter = Reporter(config['output_report'])
        reporter.generate(enriched_matches, threshold=config['threshold'])
        print("Done.")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
