from collections import defaultdict
import numpy as np

def create_vocabulary(sentences):
    vocab = {}
    idx = 0

    for sentence in sentences:
        # Split sentence into words and convert to lowercase for consistency
        words = sentence.lower().split()
        for word in words:
            if word not in vocab:
                vocab[word] = idx
                idx += 1

    return vocab

def bag_of_words_vector(sentence, vocab):
    bow_vector = np.zeros(len(vocab), dtype=int)

    words = sentence.lower().split()

    for word in words:
        if word in vocab:
            bow_vector[vocab[word]] += 1

    return bow_vector


# Step 1: Create vocabulary from training sentences
sentences = [
    "I love apples",
    "Apples are great",
    "I enjoy eating healthy food",
    "Food is essential for life"
]

vocab = create_vocabulary(sentences)
print(f"Vocabulary: {vocab}")

# Step 2: Convert a sentence into a Bag of Words vector
example_sentence = "I love eating apples"
bow_vector = bag_of_words_vector(example_sentence, vocab)
print(f"Bag of Words Vector for '{example_sentence}': {bow_vector}")
