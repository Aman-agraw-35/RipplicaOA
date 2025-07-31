import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Paths & model
DB_PATH = 'queries.json'
EMBED_DIM = 384
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize FAISS index
index = faiss.IndexFlatL2(EMBED_DIM)
cache = []  # List of dicts: {query, summary, embedding}

# Load existing cache
if os.path.exists(DB_PATH):
    with open(DB_PATH, 'r') as f:
        cache = json.load(f)
    # Rebuild index
    embeddings = np.array([item['embedding'] for item in cache], dtype='float32')
    if len(embeddings) > 0:
        index.add(embeddings)


def save_to_db(query: str, summary: str, embedding: list) -> None:
    """Append new query to cache file and FAISS index."""
    cache.append({'query': query, 'summary': summary, 'embedding': embedding})
    # Save to JSON
    with open(DB_PATH, 'w') as f:
        json.dump(cache, f, indent=2)
    # Add to FAISS
    index.add(np.array([embedding], dtype='float32'))