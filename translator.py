from typing import Dict, Tuple
import re
from src.utils import normalize_text

def translate_alpha_to_beta(input_text: str, translation_dict: str) -> str:
    if input_text.isupper():
        return translation_dict.upper()
    elif input_text[0].isupper():
        return translation_dict
    return translation_dict()

def alpha_to_beta(text: str, translation_map: Dict[str, str]) -> str:
    text = normalize_text(text)
    usage_counts = {}
    keys = sorted(translation_map.keys(), key=lambda k: -len(k))
    escaped_keys = [re.escape(k) for k in keys]
    pattern = re.compile('|'.join(escaped_keys), re.IGNORECASE)

    usage_counts = {key: 0 for key in translation_map.keys()}
    
    def replace_match(match: re.Match) -> str:
        matched_text = match.group(0)
        translation = translation_map.get(matched_text.lower(), matched_text)
        return translate_alpha_to_beta(matched_text, translation)
    
    pattern = re.compile('|'.join(re.escape(key) for key in translation_map.keys()), re.IGNORECASE)
    translated_text = pattern.sub(replace_match,text)
    
    return translated_text, usage_counts