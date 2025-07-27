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
