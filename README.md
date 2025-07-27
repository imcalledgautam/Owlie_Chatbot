# 🦉 Groq-Owlie-Demo

This project showcases a semantic search chatbot powered by Groq's ultra-fast inference and sentence-transformer embeddings. The chatbot, Owlie, answers questions based on chunked JSON documents using a combination of FAISS search and Groq API inference.

## 🚀 Features
- Dense embedding generation with SentenceTransformer
- Query normalization for better recall
- FAISS vector similarity search
- Groq API-based LLM response
- Gradio UI for simple chatbot interface

## 📁 Folder Structure
```
Groq-Owlie-Demo/
├── data/                    # Place v15_dataset.json here
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── normalizer.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── generator.py
│   └── ui.py
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
```

## 📦 Setup
```bash
git clone https://github.com/your-username/Groq-Owlie-Demo.git
cd Groq-Owlie-Demo
pip install -r requirements.txt
```

Create a `.env` file or set your API key as an environment variable:
```bash
export GROQ_API_KEY=your_groq_token
```

## 🧠 Usage
To launch CLI version:
```bash
python main.py
```

To launch chatbot UI:
```bash
python src/ui.py
```

## 📄 Sample JSON Format (data/v15_dataset.json)
```json
[
  {
    "title": "Program Overview",
    "text": "The MS in Business Analytics focuses on data-driven decision making...",
    "url": "https://jsom.utdallas.edu"
  }
]
```

## 📝 License
MIT © 2025 Gautam Naik
