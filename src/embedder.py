# src/embedder.py
from sentence_transformers import SentenceTransformer
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(texts: List[str]):
    return model.encode(texts, show_progress_bar=True)
