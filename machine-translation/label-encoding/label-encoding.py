def label_encode(sequence, vocab):
    encoded_sequence = []
    
    for token in sequence:
        token = token.lower() 
        if token in vocab:
            encoded_sequence.append(vocab[token])
        elif '<UNK>' in vocab:
            encoded_sequence.append(vocab['<UNK>'])
        else:
          
            print(f"Warning: Token '{token}' not found in vocabulary and '<UNK>' is not defined.")
            encoded_sequence.append(-1) 

    return encoded_sequence
