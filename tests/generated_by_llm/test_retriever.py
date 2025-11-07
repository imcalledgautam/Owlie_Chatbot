# src/retriever_test.py
import pytest
import numpy as np
from unittest.mock import MagicMock
import faiss
import pandas as pd

@pytest.fixture
def create_faiss_index_mock():
    return MagicMock()

@pytest.fixture
def search_similar_chunks_mock():
    return MagicMock()

def test_create_faiss_index(create_faiss_index_mock):
    embeddings = np.random.rand(10, 5)
    expected_result = faiss.IndexFlatL2(embeddings.shape[1])
    create_faiss_index_mock.return_value = expected_result
    index = create_faiss_index(embeddings)
    assert index is expected_result

def test_search_similar_chunks(search_similar_chunks_mock):
    embeddings = np.random.rand(10, 5)
    query_embedding = np.random.rand(5)
    top_k = 3
    expected_result = (np.array([1, 2, 5]), np.array([0, 1, 2]))
    search_similar_chunks_mock.return_value = expected_result
    distances, indices = search_similar_chunks(index, query_embedding, top_k)
    assert np.array_equal(distances, expected_result[0])
    assert np.array_equal(indices, expected_result[1])

def test_create_faiss_index_error(create_faiss_index_mock):
    with pytest.raises(ValueError):
        create_faiss_index(np.random.rand(5, 4))  # Incorrect dimension

def test_search_similar_chunks_error(search_similar_chunks_mock):
    embeddings = np.random.rand(10, 5)
    query_embedding = np.random.rand(6)
    expected_result = (np.array([1, 2, 5]), np.array([0, 1, 2]))
    search_similar_chunks_mock.return_value = expected_result
    with pytest.raises(ValueError):
        search_similar_chunks(index, query_embedding, -1)  # Negative top_k

def test_search_similar_chunks_empty_index(search_similar_chunks_mock):
    embeddings = np.random.rand(0, 5)
    query_embedding = np.random.rand(5)
    expected_result = (np.array([]), np.array([]))
    search_similar_chunks_mock.return_value = expected_result
    distances, indices = search_similar_chunks(index, query_embedding)
    assert np.array_equal(distances, expected_result[0])
    assert np.array_equal(indices, expected_result[1])

def test_search_similar_chunks_empty_query(search_similar_chunks_mock):
    embeddings = np.random.rand(10, 5)
    query_embedding = np.empty((0,))
    top_k = 3
    expected_result = (np.array([]), np.array([]))
    search_similar_chunks_mock.return_value = expected_result
    distances, indices = search_similar_chunks(index, query_embedding, top_k)
    assert np.array_equal(distances, expected_result[0])
    assert np.array_equal(indices, expected_result[1])

def test_search_similar_chunks_empty_embeddings(search_similar_chunks_mock):
    embeddings = np.empty((0, 5))
    query_embedding = np.random.rand(5)
    top_k = 3
    expected_result = (np.array([]), np.array([]))
    search_similar_chunks_mock.return_value = expected_result
    distances, indices = search_similar_chunks(index, query_embedding, top_k)
    assert np.array_equal(distances, expected_result[0])
    assert np.array_equal(indices, expected_result[1])