# tests/data_loader_test.py
import pytest
from src.data_loader import load_json_to_dataframe, chunk_text, preprocess_documents
from config import JSON_PATH, CHUNK_SIZE, OVERLAP
from typing import List

@pytest.fixture
def mock_df():
    return pd.DataFrame({
        "title": ["Title 1", "Title 2"],
        "text": ["Text 1", "Text 2"]
    })

def test_load_json_to_dataframe(mock_df):
    with pytest.raises(FileNotFoundError):
        load_json_to_dataframe()

def test_chunk_text():
    chunks = chunk_text(text)
    assert len(chunks) == 3
    assert chunks[0] == "Hello world!"
    assert chunks[2] == "a test."

def test_preprocess_documents(mock_df):
    documents = preprocess_documents(mock_df)
    assert len(documents) == 2
    assert documents[0]["metadata"]["source"] == "http://example.com"
    assert documents[1]["metadata"]["source"] == "http://example.com"

def test_preprocess_documents_error_handling(mock_df):
    with pytest.raises(ValueError):
        preprocess_documents(pd.DataFrame({}))

def test_preprocess_documents_edge_cases():
    documents = preprocess_documents(pd.DataFrame({
        "title": ["Title 1"],
        "text": []
    }))
    assert len(documents) == 0

if __name__ == "__main__":
    pytest.main()