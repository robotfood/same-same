import numpy as np
from same_same.vectorizer import Vectorizer

def test_vectorization():
    v = Vectorizer(model_name="en_core_web_md")
    texts = ["Broken signal", "Track fault"]
    vectors = v.vectorize(texts)
    assert vectors.shape == (2, 300)
    assert isinstance(vectors, np.ndarray)
