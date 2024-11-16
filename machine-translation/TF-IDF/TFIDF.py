# text_preprocessor.py
import pandas as pd
import numpy as np
from cltk.tokenize.sentence import TokenizeSentence
import re
from cltk.stop.classical_hindi.stops import STOPS_LIST

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def preprocess_text(file_path, author='modi'):

    # Step 1: Load and clean the text
    hindi_text = open(file_path, 'r', encoding='utf-8').read()
    hindi_text = re.sub("[a-zA-Z0-9]+", "", hindi_text)
    
    hindi_text_cleaned = "".join([char for char in hindi_text if char not in punctuations])

    # Step 2: Tokenize sentences
    tokenizer = TokenizeSentence('hindi')
    hindi_text_tokenize = tokenizer.tokenize(hindi_text_cleaned)
    hindi_text_tokenize = pd.DataFrame(hindi_text_tokenize, columns=["words"])

    # Step 3: Calculate word frequency
    counts = pd.DataFrame()
    counts['word_frequency'] = hindi_text_tokenize['words'].value_counts()
    counts['author'] = author
    counts.reset_index(inplace=True)
    counts = counts[['author', 'index', 'word_frequency']]
    
    # Step 4: Remove stopwords
    stop_words = pd.DataFrame(STOPS_LIST)
    final_words = counts[~counts['index'].isin(stop_words[0]).dropna()]
    
    # Step 5: Calculate IDF
    idf = counts.groupby('index').author.nunique().reset_index()
    idf['idf'] = np.log(2 / idf['author'])

    # Step 6: Calculate term frequency (TF)
    tf = final_words.copy()
    tf['word_sum'] = len(hindi_text_tokenize)
    tf['term_frequency'] = tf['word_frequency'] / tf['word_sum']

    # Step 7: Calculate TF-IDF
    tf_idf = tf.merge(idf, on='index', how='left')
    tf_idf['tf_idf'] = tf_idf['term_frequency'] * tf_idf['idf']
    
    return tf_idf[['index', 'term_frequency', 'tf_idf']]

if __name__ == "__main__":
    result = preprocess_text('../data/sample_text.txt')
    print(result.head())
