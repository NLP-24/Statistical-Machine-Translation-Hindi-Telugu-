import os
import chardet
import pandas as pd
import numpy as np

# Directory paths
source_base_dir = r'D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data-aligned'  # Replace with your source folder path
destination_base_dir = r'D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data-confidence'  

# Create destination directory if it doesn't exist
os.makedirs(destination_base_dir, exist_ok=True)

# Encoding conversion process
for folder_name in os.listdir(source_base_dir):
    folder_path = os.path.join(source_base_dir, folder_name)
    
    if os.path.isdir(folder_path) and folder_name.startswith('data-'):
        print(f"\nProcessing folder: {folder_name}")
        
        dest_folder_path = os.path.join(destination_base_dir, folder_name)
        os.makedirs(dest_folder_path, exist_ok=True)
        print(f"Created destination folder: {dest_folder_path}")
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.srt'):
                file_path = os.path.join(folder_path, file_name)
                print(f"\nProcessing file: {file_name}")
                
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    result = chardet.detect(raw_data)
                    file_encoding = result['encoding']
                    print(f"Detected encoding: {file_encoding}, changing...")
                
                try:
                    with open(file_path, 'r', encoding=file_encoding) as f:
                        content = f.read()
                    print(f"Successfully changed (to UTF-8) file: {file_name}")
                except Exception as e:
                    print(f"Error reading {file_name} with encoding {file_encoding}: {e}")
                    continue  
                
                dest_file_path = os.path.join(dest_folder_path, file_name)
                with open(dest_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"File saved as UTF-8 in: {dest_file_path}")

print("\nAll .srt files have been converted to UTF-8 and saved in 'data-encoded'.")

# Function to load the dataset
def load_dataset(file_path, sep='\t', header=None):
    """
    Load the dataset with error handling.
    
    :param file_path: Path to the dataset file.
    :param sep: The delimiter for separating columns (default is tab '\t').
    :param header: Whether the file has a header row (default is None for no header).
    :return: Pandas DataFrame with 'Hindi Sentence' and 'Telugu Sentence' columns.
    """
    try:
        # Load the dataset using pandas with specified separator and header options
        df = pd.read_csv(file_path, sep=sep, header=header, names=['Hindi Sentence', 'Telugu Sentence'], encoding='utf-8')
        print(f"Successfully loaded dataset from {file_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed, check the separator or format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    # Handle missing or NaN values
    if df.isnull().values.any():
        print("Warning: Missing values found in the dataset. Filling missing values with empty strings.")
        df.fillna('', inplace=True)
    
    return df

# Tokenize the sentences by splitting on whitespace
def tokenize(sentence):
    return sentence.split()

# Calculate the length ratio between Hindi and Telugu sentences
def length_ratio(hindi_tokens, telugu_tokens):
    L_h = len(hindi_tokens)
    L_t = len(telugu_tokens)
    return L_h / L_t if L_t != 0 else np.inf

# Calculate lexical similarity (based on overlap of punctuation and digits for simplicity)
def lexical_similarity(hindi_tokens, telugu_tokens):
    # Define a simple set of characters to match (punctuation, numbers)
    common_elements = set("0123456789.,!?")
    hindi_overlap = [char for token in hindi_tokens for char in token if char in common_elements]
    telugu_overlap = [char for token in telugu_tokens for char in common_elements]
    
    overlap_count = len(set(hindi_overlap).intersection(set(telugu_overlap)))
    avg_length = (len(hindi_tokens) + len(telugu_tokens)) / 2
    return overlap_count / avg_length if avg_length != 0 else 0

# Combined confidence score formula
def confidence_score(hindi_sentence, telugu_sentence):
    # Tokenize sentences
    hindi_tokens = tokenize(hindi_sentence)
    telugu_tokens = tokenize(telugu_sentence)
    
    # Compute length ratio
    R = length_ratio(hindi_tokens, telugu_tokens)
    
    # Compute lexical similarity (optional)
    S = lexical_similarity(hindi_tokens, telugu_tokens)
    
    # Combined confidence score formula
    C = (2 / (1 + abs(R - 1))) * S
    return C

# Apply the confidence score calculation to the dataset
def compute_confidence_scores(dataset):
    dataset['Confidence'] = dataset.apply(lambda row: confidence_score(row['Hindi Sentence'], row['Telugu Sentence']), axis=1)
    return dataset

# Save the result to a new file
def save_results(dataset, output_file):
    dataset.to_csv(output_file, sep='\t', index=False)

# Main function to run the pipeline
def main(input_file, output_file):
    dataset = load_dataset(input_file)
    
    # Check if dataset is loaded successfully
    if dataset is not None:
        result = compute_confidence_scores(dataset)
        save_results(result, output_file)
        print(f"Confidence scores saved to {output_file}")
    else:
        print("Processing aborted due to an error while loading the dataset.")

# Example usage for processing the dataset
if __name__ == '__main__':
    input_file = 'dataset.tsv'  # Input file with parallel corpus
    output_file = 'dataset_with_confidence.tsv'  # Output file with confidence scores
    main(input_file, output_file)
