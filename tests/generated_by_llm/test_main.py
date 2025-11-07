import pytest
from unittest.mock import patch, MagicMock
from src.config import JSON_PATH
from src.data_loader import load_json_to_dataframe, preprocess_documents
from src.normalizer import normalize_query
from src.embedder import generate_embeddings
from src.retriever import create_faiss_index, search_similar_chunks
from src.generator import query_groq

@pytest.fixture
def mock_request():
    return MagicMock()

class TestOwlieChatbot:
    def test_load_json_to_dataframe(self):
        df = load_json_to_dataframe()
        assert isinstance(df, pd.DataFrame)

    def test_preprocess_documents(self):
        processed_docs = preprocess_documents(documents)
        assert all(isinstance(doc['text'], str) for doc in processed_docs)

    def test_normalize_query(self):
        query = "What is the weather today?"
        normalized_query = normalize_query(query)
        assert isinstance(normalized_query, str)

    def test_generate_embeddings(self):
        embeddings = generate_embeddings(texts)
        assert embeddings.shape == (2, 768)

    def test_create_faiss_index(self):
        embeddings = np.random.rand(10, 768)
        index = create_faiss_index(embeddings)
        assert isinstance(index, faiss.IndexFlatL2)

    @patch('src.retriever.requests.post')
    def test_search_similar_chunks(self, mock_requests):
        query_embedding = np.random.rand(768)
        distances, indices = search_similar_chunks(index, query_embedding, top_k=3)
        assert isinstance(distances, np.ndarray)
        assert isinstance(indices, np.ndarray)

    @patch('src.generator.query_groq')
    def test_query_groq(self, mock_query_groq):
        prompt = "What is the weather today?"
        response = query_groq(prompt, api_key="your-api-key")
        assert isinstance(response, dict)