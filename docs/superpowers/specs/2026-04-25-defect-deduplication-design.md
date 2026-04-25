# Defect Deduplication Tool Design Specification

## 1. Goal
Build a Python-based CLI tool to identify duplicate defect descriptions between two CSV files (Company vs. Vendor) using semantic similarity. The tool is designed to handle approximately 8,000 company defects and 16,000 vendor defects (128 million comparisons).

## 2. Architecture
The tool follows a "Direct Matrix" approach for maximum accuracy and semantic coverage:
1.  **Ingestion:** Load configuration from `config.json` and read defect data from two CSV files.
2.  **Vectorization:** Use spaCy's `en_core_web_md` (or `lg`) model to convert text descriptions into 300-dimensional vectors.
3.  **Computation:** Calculate a 128-million-pair similarity matrix using scikit-learn's optimized `cosine_similarity`.
4.  **Filtering:** Identify pairs with a similarity score exceeding a user-defined threshold.
5.  **Reporting:** Generate a Markdown report listing duplicate candidates.

## 3. Technical Requirements
- **Language:** Python 3.x
- **Libraries:**
    - `spacy`: NLP and vectorization.
    - `scikit-learn`: High-performance cosine similarity.
    - `pandas`: CSV data manipulation.
    - `numpy`: Matrix handling.
- **Model:** `en_core_web_md` (includes word vectors required for semantic similarity).
- **Concurrency:** Use `nlp.pipe(n_process=-1)` to utilize all available CPU cores for text processing.

## 4. Configuration (`config.json`)
The tool will look for a `config.json` file in the root directory with the following structure:
```json
{
  "company_csv_path": "path/to/company_defects.csv",
  "vendor_csv_path": "path/to/vendor_defects.csv",
  "company_desc_col": "Description",
  "vendor_desc_col": "Summary",
  "threshold": 0.85,
  "output_report": "deduplication_report.md"
}
```

## 5. Output Format
A Markdown file containing:
- Summary of the run (files compared, threshold used, total matches found).
- A table of matches:
    | Score | Company Description | Vendor Description |
    | :--- | :--- | :--- |
    | 0.92 | Signal aspect on S42 not updating... | S42 stuck at red |

## 6. Implementation Strategy
- **Phase 1: Environment Setup:** Verify Python, install dependencies, and download the spaCy model.
- **Phase 2: Data Loading:** Build the CSV loader and config parser.
- **Phase 3: Vectorization Engine:** Implement parallel text processing.
- **Phase 4: Similarity Math:** Implement matrix multiplication and threshold filtering.
- **Phase 5: Reporting:** Format and save the results to Markdown.

## 7. Constraints & Considerations
- **Memory:** The similarity matrix (8,000 x 16,000 floats) requires ~512MB of RAM. Total memory usage should remain under 4GB.
- **Domain Specifics:** The tool will handle rail-specific terms (signals, interlockings) through standard semantic similarity, with potential for regex-based ID normalization in future iterations.
