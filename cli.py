import argparse
from src.utils import load_slang
from src. translator import alpha_to_beta

def main():
    parser = argparse.ArgumentParser(description="Gen alpha translator cli")
    parser.add_argument("input_file", type=str, help="Path to the input text file containing Alpha slang.")
    parser.add_argument("output_file", type=str, help="Path to the output text file for Beta slang.")
    parser.add_argument("--slang_file", type=str, default="data/alpha_beta_slang.json", help="Path to the slang translation JSON file.")
    
    args = parser.parse_args()
    
    translation_map = load_slang(args.slang_file)
    
    with open(args.input_file, 'r', encoding='utf-8') as infile:
        input_text = infile.read()
    
    translated_text, usage_counts = alpha_to_beta(input_text, translation_map)
    
    with open(args.output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(translated_text)
    
    print("Translation complete. Usage counts:")
    for slang, count in usage_counts.items():
        print(f"{slang}: {count}")