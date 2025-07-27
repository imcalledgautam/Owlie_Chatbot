# src/embedder.py
from sentence_transformers import SentenceTransformer
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(texts: List[str]):
    return model.encode(texts, show_progress_bar=True)


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


# src/generator.py
import os
import requests

def query_groq(prompt, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are Owlie, a helpful and concise assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]


# src/ui.py
import gradio as gr
from generator import query_groq

def run_chat_interface():
    def respond(user_input):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "API key not found. Please set GROQ_API_KEY environment variable."
        return query_groq(user_input, api_key)

    iface = gr.Interface(fn=respond, inputs="text", outputs="text", title="Owlie Chatbot (Groq-powered)")
    iface.launch()

if __name__ == "__main__":
    run_chat_interface()


# main.py
import os
from src.config import JSON_PATH
from src.data_loader import load_json_to_dataframe, preprocess_documents
from src.normalizer import normalize_query
from src.embedder import generate_embeddings
from src.retriever import create_faiss_index, search_similar_chunks
from src.generator import query_groq

if __name__ == "__main__":
    # Load and preprocess data
    df = load_json_to_dataframe()
    documents = preprocess_documents(df)
    texts = [doc['text'] for doc in documents]

    # Generate embeddings and index
    embeddings = generate_embeddings(texts)
    index = create_faiss_index(embeddings)

    # Example usage
    user_query = input("Ask Owlie something: ")
    normalized_query = normalize_query(user_query)
    query_embedding = generate_embeddings([normalized_query])
    _, indices = search_similar_chunks(index, query_embedding, top_k=3)

    # Build the prompt and call Groq
    top_chunks = [documents[i]['text'] for i in indices[0]]
    context = "\n---\n".join(top_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {user_query}\nAnswer:"

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY not set.")
    else:
        answer = query_groq(prompt, api_key)
        print("\nOwlie:", answer)
