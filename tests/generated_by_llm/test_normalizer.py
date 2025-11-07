# src/test_normalizer.py
import pytest
import re
from unittest.mock import MagicMock
from src.normalizer import normalize_query

@pytest.fixture
def mock_alias_dict():
    return {
        "MS_Business_Analytics_AI": [
            "BUAN", "MSBUAN", "MSBAAI", "BAAI", "Business Analytics",
            "Business Analytics and AI", "Business Analytics & AI",
            "Business Analytics and Artificial Intelligence",
            "Masters of Science in Business Analytics and AI"
        ],
        "MS_ITM": ["ITM", "MSITM", "MS ITM", "Information Technology and Management"],
        "MS_Finance": ["Finance", "MSFinance", "MS Finance", "Financial Engineering"],
        "MS_Supply_Chain": ["Supply Chain", "SCM", "MS SCM", "MS in Supply Chain Management"],
        "MS_Marketing": ["Marketing", "MSMarketing", "MS Marketing"]
    }

@pytest.fixture
def mock_program_types():
    return [
        (r"\\b(Flex Online|Online Flex)\\b", "ProgramType_FlexOnline"),
        (r"\\b(Flex)\\b", "ProgramType_Flex"),
        (r"\\b(Cohort)\\b", "ProgramType_Cohort")
    ]

def test_normalize_query(mock_alias_dict, mock_program_types):
    text = normalize_query("Flex Online MS_Business_Analytics_AI ITM Finance SCM Marketing")
    assert text == "FlexOnline BAAI ITM Finance SCM Marketing"

    text = normalize_query("MS_Business_Analytics_AI MS_ITM")
    assert text == "BUAN ITM"

    text = normalize_query("Finance MS_Finance")
    assert text == "Finance FINANCE"

    text = normalize_query("SCM MS_Supply_Chain")
    assert text == "SCM SCM"

    text = normalize_query("Marketing MS_Marketing")
    assert text == "Marketing MARKETING"

    # Test with non-matching patterns
    mock_alias_dict["MS_NonExist"] = ["NonExist"]
    mock_program_types.append((r"\\b(NonExist)\\b", "ProgramType_NonExist"))
    text = normalize_query("NonExist MS_NonExist")
    assert text == "NonExist NonExist"

    # Test with non-matching patterns
    text = normalize_query("MS_NonExist NonExist")
    assert text == "NonExist NonExist"

    # Test with edge cases
    text = normalize_query("")
    assert text == ""

    text = normalize_query(None)
    assert text is None

    text = normalize_query(123)
    assert text is None

    # Test with regular expressions that do not match anything
    mock_alias_dict["MS_NonExist"] = []
    mock_program_types.append((r"\\b(NonExist)\\b", "ProgramType_NonExist"))
    text = normalize_query("NonExist MS_NonExist")
    assert text == "NonExist NonExist"


# src/test_normalizer.py
import pytest
import re
from unittest.mock import MagicMock
from src.normalizer import normalize_query

@pytest.fixture
def mock_alias_dict():
    return {
        "MS_Business_Analytics_AI": [
            "BUAN", "MSBUAN", "MSBAAI", "BAAI", "Business Analytics",
            "Business Analytics and AI", "Business Analytics & AI",
            "Business Analytics and Artificial Intelligence",
            "Masters of Science in Business Analytics and AI"
        ],
        "MS_ITM": ["ITM", "MSITM", "MS ITM", "Information Technology and Management"],
        "MS_Finance": ["Finance", "MSFinance", "MS Finance", "Financial Engineering"],
        "MS_Supply_Chain": ["Supply Chain", "SCM", "MS SCM", "MS in Supply Chain Management"],
        "MS_Marketing": ["Marketing", "MSMarketing", "MS Marketing"]
    }

@pytest.fixture
def mock_program_types():
    return [
        (r"\\b(Flex Online|Online Flex)\\b", "ProgramType_FlexOnline"),
        (r"\\b(Flex)\\b", "ProgramType_Flex"),
        (r"\\b(Cohort)\\b", "ProgramType_Cohort")
    ]

def test_normalize_query_edge_cases(mock_alias_dict, mock_program_types):
    # Test with empty input
    text = normalize_query("")
    assert text == ""

    # Test with None input
    text = normalize_query(None)
    assert text is None

    # Test with non-matching patterns
    mock_alias_dict["MS_NonExist"] = ["NonExist"]
    mock_program_types.append((r"\\b(NonExist)\\b", "ProgramType_NonExist"))
    text = normalize_query("NonExist MS_NonExist")
    assert text == "NonExist NonExist"

    # Test with non-matching patterns
    text = normalize_query("MS_NonExist NonExist")
    assert text == "NonExist NonExist"