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
