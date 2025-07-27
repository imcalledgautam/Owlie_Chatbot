# src/normalizer.py
import re

alias_dict = {
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

program_types = [
    (r"\\b(Flex Online|Online Flex)\\b", "ProgramType_FlexOnline"),
    (r"\\b(Flex)\\b", "ProgramType_Flex"),
    (r"\\b(Cohort)\\b", "ProgramType_Cohort")
]

def normalize_query(text):
    for canonical_name, variants in alias_dict.items():
        for variant in variants:
            pattern = r"\\b" + re.escape(variant) + r"\\b"
            text = re.sub(pattern, canonical_name, text, flags=re.IGNORECASE)
    for pattern, label in program_types:
        text = re.sub(pattern, label, text, flags=re.IGNORECASE)
    return text