import json
import re
from typing import Dict, List

WORD_BOUNDARY = r'\b'

def load_slang(path: str) -> Dict[str, str]: #We want to load the slang dictionary present along with its path, to give us a str in return.
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {k.lower(): v for k, v in data.items()}  # Normalize keys to lowercase

def normalize_text(text: str) -> str:
    text.strip() #This function is used to normalize the text by removing extra spaces and converting it to lowercase.
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text

def find_candidates(text: str, slang_dict: List[str]) -> List[str]:
    lowered = text.lower()
    matches = []
    for slang in slang_dict.keys():
        pattern = WORD_BOUNDARY + re.escape(slang) + WORD_BOUNDARY
        if re.search(pattern, text, flags=re.IGNORECASE):
            matches.append(slang)
    return sorted(matches, slang=lambda k: -len(k))  # Sort by length descending