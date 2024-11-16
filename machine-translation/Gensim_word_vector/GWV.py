from gensim.models import Word2Vec
from gensim.models import FastText

def train_word2vec(sentences, vector_size=100, window=5, min_count=1, workers=4):
    model = Word2Vec(sentences=sentences, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    return model

def train_fasttext(sentences, vector_size=100, window=5, min_count=1, workers=4):
    model = FastText(sentences=sentences, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    return model

def apply_word_vectors(sentences, model):
    vectorized_sentences = []
    for sentence in sentences:
        vectorized_sentence = [model.wv[word] for word in sentence.split() if word in model.wv]
        vectorized_sentences.append(vectorized_sentence)
    return vectorized_sentences


# Usage :-
    # pip install gensim