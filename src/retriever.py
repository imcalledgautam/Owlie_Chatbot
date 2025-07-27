# src/retriever.py
import faiss
import numpy as np

def create_faiss_index(embeddings: np.ndarray):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_similar_chunks(index, query_embedding: np.ndarray, top_k=5):
    distances, indices = index.search(query_embedding, top_k)
    return distances, indices