# same-same Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python-based CLI tool to identify duplicate defect descriptions between two CSV files using semantic similarity.

**Architecture:** A Direct Matrix approach using spaCy for vectorization and scikit-learn for optimized cosine similarity computation.

**Tech Stack:** Python 3.x, spaCy, scikit-learn, pandas, numpy, pytest.

---

### Task 1: Project Initialization & Environment Setup

**Files:**
- Create: `pyproject.toml`
- Create: `requirements.txt`
- Create: `README.md`

- [ ] **Step 1: Create `pyproject.toml`**

```toml
[project]
name = "same-same"
version = "0.1.0"
description = "Semantic defect deduplication tool"
dependencies = [
    "spacy>=3.0.0",
    "scikit-learn",
    "pandas",
    "numpy",
]

[project.scripts]
same-same = "same_same.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: Create `requirements.txt`**

```text
spacy>=3.0.0
scikit-learn
pandas
numpy
pytest
```

- [ ] **Step 3: Setup virtual environment and install dependencies**

Run: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python3 -m spacy download en_core_web_md`
Expected: Successful installation of libraries and spaCy model.

- [ ] **Step 4: Commit**

```bash
git add pyproject.toml requirements.txt
git commit -m "chore: initialize project and dependencies"
```

---

### Task 2: Configuration Loader

**Files:**
- Create: `src/same_same/config.py`
- Test: `tests/test_config.py`

- [ ] **Step 1: Write failing test for config loading**

```python
import json
import os
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_config.py`
Expected: FAIL (ModuleNotFoundError)

- [ ] **Step 3: Implement `load_config`**

```python
import json

def load_config(path):
    with open(path, 'r') as f:
        return json.load(f)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_config.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/same_same/config.py tests/test_config.py
git commit -m "feat: add config loader"
```

---

### Task 3: Data Loader

**Files:**
- Create: `src/same_same/data_loader.py`
- Test: `tests/test_data_loader.py`

- [ ] **Step 1: Write failing test for CSV loading**

```python
import pandas as pd
from same_same.data_loader import load_data

def test_load_data(tmp_path):
    df_data = pd.DataFrame({"Description": ["Defect 1", "Defect 2"]})
    csv_path = tmp_path / "test.csv"
    df_data.to_csv(csv_path, index=False)
    
    df = load_data(str(csv_path))
    assert len(df) == 2
    assert df.iloc[0]["Description"] == "Defect 1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_data_loader.py`
Expected: FAIL

- [ ] **Step 3: Implement `load_data`**

```python
import pandas as pd

def load_data(path):
    return pd.read_csv(path)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_data_loader.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/same_same/data_loader.py tests/test_data_loader.py
git commit -m "feat: add data loader"
```

---

### Task 4: Vectorization Engine

**Files:**
- Create: `src/same_same/vectorizer.py`
- Test: `tests/test_vectorizer.py`

- [ ] **Step 1: Write failing test for vectorization**

```python
import numpy as np
from same_same.vectorizer import Vectorizer

def test_vectorization():
    v = Vectorizer(model_name="en_core_web_md")
    texts = ["Broken signal", "Track fault"]
    vectors = v.vectorize(texts)
    assert vectors.shape == (2, 300)
    assert isinstance(vectors, np.ndarray)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_vectorizer.py`
Expected: FAIL

- [ ] **Step 3: Implement `Vectorizer` class**

```python
import spacy
import numpy as np

class Vectorizer:
    def __init__(self, model_name="en_core_web_md"):
        self.nlp = spacy.load(model_name)
    
    def vectorize(self, texts):
        # Use nlp.pipe for efficiency
        docs = self.nlp.pipe(texts, n_process=-1)
        return np.array([doc.vector for doc in docs])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_vectorizer.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/same_same/vectorizer.py tests/test_vectorizer.py
git commit -m "feat: add vectorization engine"
```

---

### Task 5: Similarity Computation

**Files:**
- Create: `src/same_same/matcher.py`
- Test: `tests/test_matcher.py`

- [ ] **Step 1: Write failing test for matching**

```python
import numpy as np
from same_same.matcher import Matcher

def test_matching():
    # Mock vectors
    company_vecs = np.array([[1.0, 0.0], [0.0, 1.0]])
    vendor_vecs = np.array([[0.9, 0.1], [0.1, 0.9], [0.5, 0.5]])
    
    matcher = Matcher(threshold=0.8)
    matches = matcher.find_matches(company_vecs, vendor_vecs)
    
    # Expected: (0, 0) and (1, 1) are matches
    assert len(matches) == 2
    assert matches[0]['company_idx'] == 0
    assert matches[0]['vendor_idx'] == 0
    assert matches[0]['score'] >= 0.8
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_matcher.py`
Expected: FAIL

- [ ] **Step 3: Implement `Matcher` class**

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Matcher:
    def __init__(self, threshold=0.85):
        self.threshold = threshold
    
    def find_matches(self, company_vecs, vendor_vecs):
        sim_matrix = cosine_similarity(company_vecs, vendor_vecs)
        matches = []
        rows, cols = np.where(sim_matrix >= self.threshold)
        for r, c in zip(rows, cols):
            matches.append({
                'company_idx': int(r),
                'vendor_idx': int(c),
                'score': float(sim_matrix[r, c])
            })
        # Sort by score descending
        matches.sort(key=lambda x: x['score'], reverse=True)
        return matches
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_matcher.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/same_same/matcher.py tests/test_matcher.py
git commit -m "feat: add similarity computation"
```

---

### Task 6: Reporting

**Files:**
- Create: `src/same_same/reporter.py`
- Test: `tests/test_reporter.py`

- [ ] **Step 1: Write failing test for reporting**

```python
from same_same.reporter import Reporter

def test_generate_report(tmp_path):
    matches = [
        {'score': 0.95, 'company_desc': 'C1', 'vendor_desc': 'V1'},
        {'score': 0.90, 'company_desc': 'C2', 'vendor_desc': 'V2'}
    ]
    output_path = tmp_path / "report.md"
    reporter = Reporter(output_path)
    reporter.generate(matches, threshold=0.85)
    
    content = output_path.read_text()
    assert "# same-same Deduplication Report" in content
    assert "| 0.95 | C1 | V1 |" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_reporter.py`
Expected: FAIL

- [ ] **Step 3: Implement `Reporter` class**

```python
class Reporter:
    def __init__(self, output_path):
        self.output_path = output_path
    
    def generate(self, matches, threshold):
        lines = [
            "# same-same Deduplication Report",
            f"\n- **Threshold:** {threshold}",
            f"- **Total Matches:** {len(matches)}",
            "\n| Score | Company Description | Vendor Description |",
            "| :--- | :--- | :--- |"
        ]
        for m in matches:
            lines.append(f"| {m['score']:.4f} | {m['company_desc']} | {m['vendor_desc']} |")
        
        with open(self.output_path, 'w') as f:
            f.write("\n".join(lines))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_reporter.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/same_same/reporter.py tests/test_reporter.py
git commit -m "feat: add reporting engine"
```

---

### Task 7: CLI Integration

**Files:**
- Create: `src/same_same/cli.py`
- Create: `src/same_same/__init__.py`
- Test: `tests/test_cli.py`

- [ ] **Step 1: Create `src/same_same/__init__.py`**

```python
# Leave empty or add package version
__version__ = "0.1.0"
```

- [ ] **Step 2: Implement CLI entry point in `src/same_same/cli.py`**

```python
import sys
import argparse
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
```

- [ ] **Step 3: Verify the CLI with a small test run**

1. Create a dummy `config.json` and CSV files.
2. Run `python3 src/same_same/cli.py --config dummy_config.json`.
3. Verify output report.

- [ ] **Step 4: Commit**

```bash
git add src/same_same/cli.py src/same_same/__init__.py
git commit -m "feat: add CLI entry point"
```
