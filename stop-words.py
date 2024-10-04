import os
import pandas as pd

source_base_dir = 'data-align'
destination_base_dir = 'data-stopwords-cleaned'
os.makedirs(destination_base_dir, exist_ok=True)

hindi_stopwords = set([
    'और', 'से', 'है', 'यह', 'था', 'थे', 'का', 'कि', 'पर', 'के', 'लिए', 'एक', 'भी', 'जो', 'में', 'हूं', 'कर', 'नहीं', 'तो'
])

telugu_stopwords = set([
    'అందు', 'ఏది', 'ఎక్కడ', 'ఏక', 'ఎక్కడివారు', 'ఎలాగైనా', 'ఎలాగూ', 'కానీ', 'నాకు', 'మీకు', 'మరి', 'ముందు', 'నేను', 'వద్ద', 'వారు', 'చెప్పండి', 'కూడా', 'గురించి'
])

def remove_stopwords(sentence, stop_words):
    words = sentence.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

for file_name in os.listdir(source_base_dir):
    if file_name.endswith('.tsv'):
        file_path = os.path.join(source_base_dir, file_name)
        print(f"Processing {file_name}")

        df = pd.read_csv(file_path, sep='\t', names=['Hindi Sentence', 'Telugu Sentence'], encoding='utf-8')

        df['Hindi Sentence'] = df['Hindi Sentence'].apply(lambda x: remove_stopwords(str(x), hindi_stopwords))
        df['Telugu Sentence'] = df['Telugu Sentence'].apply(lambda x: remove_stopwords(str(x), telugu_stopwords))

        cleaned_file_path = os.path.join(destination_base_dir, file_name)
        df.to_csv(cleaned_file_path, sep='\t', index=False, header=False)
        print(f"Saved cleaned file: {cleaned_file_path}")

print("Stop word removal completed.")
