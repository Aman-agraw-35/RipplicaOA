from sentence_transformers import SentenceTransformer
import numpy as np
from db import index, cache, save_to_db

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')


def embed_text(text: str) -> np.ndarray:
    """Generate embedding vector for the given text."""
    vec = model.encode([text])[0]
    return vec.astype('float32')


def find_similar_query(query: str, threshold: float = 0.2):
    """
    Returns cached summary if similarity below threshold, else None.
    """
    if not cache:
        return None
    vec = embed_text(query)
    distances, indices = index.search(np.array([vec]), k=1)
    if distances[0][0] < threshold:
        return cache[indices[0][0]]['summary']
    return None


def save_query(query: str, summary: str) -> None:
    """
    Save new query, summary, and embedding to DB and index.
    """
    embedding = embed_text(query).tolist()
    save_to_db(query, summary, embedding)