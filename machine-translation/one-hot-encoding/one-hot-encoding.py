import numpy as np
import torch

def one_hot_encode(sequence, vocab_size):
    one_hot = np.zeros((len(sequence), vocab_size), dtype=np.float32)
    
    for idx, token_idx in enumerate(sequence):
        if token_idx < vocab_size:
            one_hot[idx, token_idx] = 1.0

    return torch.tensor(one_hot)