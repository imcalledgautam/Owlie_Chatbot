# src/data_loader.py
import json
import pandas as pd
from config import JSON_PATH, CHUNK_SIZE, OVERLAP
from typing import List


def load_json_to_dataframe():
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> List[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks

def preprocess_documents(df: pd.DataFrame):
    documents = []
    for _, row in df.iterrows():
        title = row.get("title") or ""
        text = row.get("text") or ""
        url = row.get("url") or ""
        full_text = f"{title}\n{text}"
        for chunk in chunk_text(full_text):
            documents.append({
                "text": chunk,
                "metadata": {"source": url}
            })
    return documents