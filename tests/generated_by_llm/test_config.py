import pytest
from src.config import CHUNK_SIZE, OVERLAP, JSON_PATH

def test_chunk_size():
    """Test that CHUNK_SIZE constant has expected value."""
    assert CHUNK_SIZE == 600, "Chunk size should be 600"

def test_overlap():
    """Test that OVERLAP constant has expected value."""
    assert OVERLAP == 200, "Overlap should be 200"

def test_json_path():
    """Test that JSON_PATH constant has expected value."""
    assert JSON_PATH == "data/v15_dataset.json", "JSON path should be 'data/v15_dataset.json'"

def test_constants_are_integers():
    """Test that numeric constants are proper integers."""
    assert isinstance(CHUNK_SIZE, int), "CHUNK_SIZE should be an integer"
    assert isinstance(OVERLAP, int), "OVERLAP should be an integer"

def test_constants_are_positive():
    """Test that numeric constants are positive values."""
    assert CHUNK_SIZE > 0, "CHUNK_SIZE should be positive"
    assert OVERLAP >= 0, "OVERLAP should be non-negative"

def test_json_path_is_string():
    """Test that JSON_PATH is a string."""
    assert isinstance(JSON_PATH, str), "JSON_PATH should be a string"
    assert JSON_PATH.endswith('.json'), "JSON_PATH should end with .json"