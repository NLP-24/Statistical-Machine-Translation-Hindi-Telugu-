import pickle
from collections import defaultdict

class Vocab:
    def __init__(self):
        self.token_to_index = {}
        self.index_to_token = {}
        self.freq = defaultdict(int)

    def build_vocab(self, sentences):
        self.token_to_index = {'<pad>': 0, '<sos>': 1, '<eos>': 2, '<unk>': 3}
        self.index_to_token = {v: k for k, v in self.token_to_index.items()}

        idx = 4
        for sentence in sentences:
            for token in sentence.split():
                if token not in self.token_to_index:
                    self.token_to_index[token] = idx
                    self.index_to_token[idx] = token
                    idx += 1

    def encode(self, sentence):
        return [self.token_to_index.get(token, 3) for token in sentence.split()]

    def decode(self, indices):
        return ' '.join([self.index_to_token[idx] for idx in indices if idx > 2])

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)

    def __len__(self):
        return len(self.token_to_index)
