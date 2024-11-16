import torch
from models.transformer_model import TransformerModel
from vocab import Vocab
import re
import unicodedata

src_vocab = Vocab.load('machine-translation\\vocab\\src_vocab.pkl')
tgt_vocab = Vocab.load('machine-translation\\vocab\\tgt_vocab.pkl')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = TransformerModel(len(src_vocab), len(tgt_vocab)).to(device)
model.load_state_dict(torch.load('testing\models\model_weights_(1).pth', map_location=device, weights_only=True))
model.eval()

def clean_translation(sentence):

    sentence = unicodedata.normalize('NFKC', sentence)
    
    sentence = re.sub(r'(\w)\1+', r'\1', sentence)
    
    words = sentence.split()
    cleaned_words = []
    for word in words:
        if not cleaned_words or word != cleaned_words[-1]:
            cleaned_words.append(word)
    cleaned_sentence = ' '.join(cleaned_words)
    
    return cleaned_sentence

def translate_sentence(sentence, max_length=50):
    src_tensor = torch.tensor([1] + src_vocab.encode(sentence) + [2]).unsqueeze(0).to(device)

    tgt_tensor = torch.tensor([[1]]).to(device)
    generated_indices = []

    for _ in range(max_length):
        output = model(src_tensor, tgt_tensor)
        
        next_token = torch.argmax(output[:, -1, :], dim=-1).item()
        generated_indices.append(next_token)

        if next_token == 2:
            break
        
        tgt_tensor = torch.cat([tgt_tensor, torch.tensor([[next_token]]).to(device)], dim=1)

    translated_sentence = tgt_vocab.decode(generated_indices)
    
    translated_sentence = clean_translation(translated_sentence)
    
    return translated_sentence

print(translate_sentence("मेरा स्कूल पर छोटा व बड़ा"))