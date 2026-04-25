import spacy
import numpy as np
from typing import List

class Vectorizer:
    """A class to handle text vectorization using spaCy."""
    
    def __init__(self, model_name: str = "en_core_web_md"):
        """Initialize the vectorizer with a spaCy model, disabling unused components."""
        self.nlp = spacy.load(model_name, disable=["ner", "parser", "lemmatizer", "attribute_ruler"])
    
    def vectorize(self, texts: List[str]) -> np.ndarray:
        """
        Convert a list of strings into a 2D numpy array of vectors.
        Uses nlp.pipe with n_process=-1 for parallel processing.
        """
        if not texts:
            return np.empty((0, 300))
        docs = self.nlp.pipe(texts, n_process=-1)
        return np.array([doc.vector for doc in docs])
