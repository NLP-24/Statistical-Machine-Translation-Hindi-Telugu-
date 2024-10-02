import os
import re
from typing import List, Dict, Tuple
from dataclasses import dataclass
from indicnlp.tokenize import indic_tokenize
from sacremoses import MosesPunctNormalizer

@dataclass
class SubtitleBlock:
    index: int
    timestamp: str
    text: str
    tokenized_text: str = ""

class SRTTokenizer:
    def __init__(self):
        self.mpn = MosesPunctNormalizer()
    
    def preprocess_text(self, text: str, language: str) -> str:
        text = self.mpn.normalize(text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def tokenize(self, text: str, language: str) -> List[str]:
        preprocessed_text = self.preprocess_text(text, language)
        tokens = indic_tokenize.trivial_tokenize(preprocessed_text, lang=language)
        return tokens
    
    def parse_srt_file(self, file_path: str) -> List[SubtitleBlock]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split the content into subtitle blocks
        blocks = re.split(r'\n\n+', content.strip())
        subtitle_blocks = []
        
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) >= 3:
                try:
                    index = int(lines[0])
                    timestamp = lines[1]
                    text = ' '.join(lines[2:])
                    subtitle_blocks.append(SubtitleBlock(index, timestamp, text))
                except ValueError:
                    # Skip malformed blocks
                    continue
        
        return subtitle_blocks
    
    def tokenize_srt_blocks(self, blocks: List[SubtitleBlock], language: str) -> List[SubtitleBlock]:
        for block in blocks:
            tokens = self.tokenize(block.text, language)
            block.tokenized_text = ' '.join(tokens)
        return blocks
    
    def write_tokenized_srt(self, blocks: List[SubtitleBlock], output_file: str):
        with open(output_file, 'w', encoding='utf-8') as f:
            for block in blocks:
                f.write(f"{block.index}\n")
                f.write(f"{block.timestamp}\n")
                f.write(f"{block.tokenized_text}\n\n")

class DataProcessor:
    def __init__(self, input_data_dir: str, output_data_dir: str):
        self.input_data_dir = input_data_dir
        self.output_data_dir = output_data_dir
        self.tokenizer = SRTTokenizer()
    
    def ensure_output_directory(self, folder_index: str):
        output_folder = os.path.join(self.output_data_dir, folder_index)
        os.makedirs(output_folder, exist_ok=True)
        return output_folder
    
    def process_srt_file(self, input_file: str, output_file: str, language: str):
        blocks = self.tokenizer.parse_srt_file(input_file)
        tokenized_blocks = self.tokenizer.tokenize_srt_blocks(blocks, language)
        self.tokenizer.write_tokenized_srt(tokenized_blocks, output_file)
    
    def process_all_files(self):
        for folder in sorted(os.listdir(self.input_data_dir), key=int):
            folder_path = os.path.join(self.input_data_dir, folder)
            
            if os.path.isdir(folder_path):
                hindi_file = os.path.join(folder_path, f'hin-{folder}.srt')
                telugu_file = os.path.join(folder_path, f'tel-{folder}.srt')
                
                if os.path.exists(hindi_file) and os.path.exists(telugu_file):
                    output_folder = self.ensure_output_directory(folder)
                    
                    output_hindi = os.path.join(output_folder, f'hin-{folder}.srt')
                    output_telugu = os.path.join(output_folder, f'tel-{folder}.srt')
                    
                    self.process_srt_file(hindi_file, output_hindi, 'hi')
                    self.process_srt_file(telugu_file, output_telugu, 'te')
                    
                    print(f"Processed folder {folder}")

def main():
    # Example usage
    input_dir = 'data'
    output_dir = 'tokenized_data_4'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    processor = DataProcessor(input_dir, output_dir)
    processor.process_all_files()
    
    print("Tokenization complete. Tokenized files are in the 'tokenized_data' directory.")

if __name__ == "__main__":
    main()