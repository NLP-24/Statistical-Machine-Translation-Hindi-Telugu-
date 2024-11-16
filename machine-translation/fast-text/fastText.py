from gensim.models import FastText
import numpy as np

def train_fasttext_embeddings(sentences):

    print("Tokenizing and preprocessing sentences...")
    tokenized_sentences = [sentence.lower().split() for sentence in sentences]

    print("Training FastText model...")
    fasttext_model = FastText(
        sentences=tokenized_sentences,
        vector_size=100,   
        window=5,          
        min_count=1,       
        sg=1,            
        workers=4          
    )
    
    fasttext_model.train(tokenized_sentences, total_examples=len(tokenized_sentences), epochs=10)
    

    print("Generating embeddings for each sentence...")
    sentence_embeddings = {}
    for sentence in sentences:
        tokenized_sentence = sentence.lower().split()
        embedding_vector = get_sentence_embedding(tokenized_sentence, fasttext_model)
        sentence_embeddings[sentence] = embedding_vector

    print("FastText model training complete.")
    return fasttext_model, sentence_embeddings

def get_sentence_embedding(sentence, model):

  
    embeddings = []
    for word in sentence:
        if word in model.wv:
            embeddings.append(model.wv[word])
        else:
            embeddings.append(np.zeros(model.vector_size))  
    
    if embeddings:
        embedding_vector = np.mean(embeddings, axis=0)
    else:
        embedding_vector = np.zeros(model.vector_size)  

    return embedding_vector