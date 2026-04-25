from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Dict

class Matcher:
    """A class to handle semantic similarity matching between vectors."""
    
    def __init__(self, threshold: float = 0.85):
        """Initialize the matcher with a similarity threshold."""
        self.threshold = threshold
    
    def find_matches(self, company_vecs: np.ndarray, vendor_vecs: np.ndarray) -> List[Dict]:
        """
        Compute similarity between two sets of vectors and return matches above threshold.
        Returns a list of dicts sorted by score descending.
        """
        if company_vecs.size == 0 or vendor_vecs.size == 0:
            return []
            
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
