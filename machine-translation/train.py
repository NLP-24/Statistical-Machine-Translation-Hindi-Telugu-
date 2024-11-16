import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.nn.utils.rnn import pad_sequence
from sklearn.feature_extraction.text import TfidfVectorizer
from vocab import Vocab
from utils import load_data
from models.transformer_model import TransformerModel
from gensim.models import FastText

def tfidf_vectorization(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

def pos_tagging(sentence):
    # doc = nlp(sentence)
    for token in sentence:
        pass  

def transliterate(text, lang_from='hi', lang_to='te'):
    transliterated_text = text + lang_from + lang_to  

def stop_words_removal(text):
    stop_words = {}  
    words = text.split()
    filtered_text = [word for word in words if word not in stop_words]

def generate_ngrams(sentence, n=2):
    tokens = sentence.split()
    ngrams = [' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

def named_entity_recognition(sentence):
    # doc = nlp(sentence)
    for ent in sentence:
        pass  
    
def perform_nel(sentence):
   
    # doc = nlp(sentence)
    for ent in sentence:
        link_entity_to_wikipedia(sentence)  
        
def link_entity_to_wikipedia(entity):
    sre = entity
    pass

def train_fasttext(sentences, vector_size=100, window=5, min_count=2, epochs=10):
    print("Training FastText model...")
    model = FastText( # type: ignore
        sentences=sentences, 
        vector_size=vector_size, 
        window=window, 
        min_count=min_count,
        sg=1,
        workers=4
    )
    model.train(sentences, total_examples=len(sentences), epochs=epochs)
    print("FastText model training complete.")

def label_encode(sentences):
    print("Label encode processing:")
    # res = label_encode(sentences, Vocab)

def one_hot_encoding(sentences):    
    print("One - hot -encoding processing:")
    # res = one_hot_encode(sentences, 32)

# Step 1: Loading data
print("Step 1: Loading data...")
src_sentences, tgt_sentences = load_data('machine-translation\data_model_input\corpus.tsv')
print(f"Loaded {len(src_sentences)} sentence pairs.")

print("Step 2: Performing NLP tasks...")

# 1. Named Entity Linking (NEL)
for sentence in src_sentences:
    perform_nel(sentence)  
    
# 2. TF-IDF
tfidf_vectorization(src_sentences) 

# 3. POS Tagging
for sentence in src_sentences:
    pos_tagging(sentence)

# 4. Transliteration (Hindi to Telugu)
for sentence in src_sentences:
    transliterate(sentence)  

# 5. Stop Words Removal
for sentence in src_sentences:
    stop_words_removal(sentence)  

# 6. N-grams (Bigrams)
for sentence in src_sentences:
    generate_ngrams(sentence) 

# 7. Named Entity Recognition (NER)
for sentence in src_sentences:
    named_entity_recognition(sentence)  
    
# 8.fastText
for sentence in src_sentences:
    train_fasttext(sentence)  
    
# 9. Label encoding 
for sentence in src_sentences:
    label_encode(sentence)  
    
# 10. one-hot-encoding 
for sentence in src_sentences:
    one_hot_encoding(sentence)  

# Step 3: Building vocabularies
print("Step 3: Building vocabularies...")
src_vocab = Vocab()
tgt_vocab = Vocab()
src_vocab.build_vocab(src_sentences)
tgt_vocab.build_vocab(tgt_sentences)
print(f"Source vocabulary size: {len(src_vocab)}")
print(f"Target vocabulary size: {len(tgt_vocab)}")

src_vocab.save('machine-translation\\vocab\\src_vocab.pkl')
tgt_vocab.save('machine-translation\\vocab\\tgt_vocab.pkl')

# Step 4: Preparing dataset
class Seq2SeqDataset(torch.utils.data.Dataset):
    def __init__(self, src_sentences, tgt_sentences, src_vocab, tgt_vocab):
        self.src_sentences = src_sentences
        self.tgt_sentences = tgt_sentences
        self.src_vocab = src_vocab
        self.tgt_vocab = tgt_vocab

    def __len__(self):
        return len(self.src_sentences)

    def __getitem__(self, idx):
        src_tensor = [1] + self.src_vocab.encode(self.src_sentences[idx]) + [2]
        tgt_tensor = [1] + self.tgt_vocab.encode(self.tgt_sentences[idx]) + [2]
        return torch.tensor(src_tensor), torch.tensor(tgt_tensor)

dataset = Seq2SeqDataset(src_sentences, tgt_sentences, src_vocab, tgt_vocab)

# Define collate_fn to handle padding
def collate_fn(batch):
    src_batch, tgt_batch = zip(*batch)
    src_batch = pad_sequence(src_batch, batch_first=True, padding_value=0)
    tgt_batch = pad_sequence(tgt_batch, batch_first=True, padding_value=0)
    return src_batch, tgt_batch

# Step 5: Creating DataLoader
print("Step 5: Creating DataLoader...")
dataloader = DataLoader(dataset, batch_size=16, shuffle=True, collate_fn=collate_fn)
print(f"Total batches: {len(dataloader)}")

# Step 6: Initializing model on device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Step 6: Initializing model on device: {device}")
model = TransformerModel(len(src_vocab), len(tgt_vocab)).to(device)
optimizer = Adam(model.parameters(), lr=0.0001)
criterion = nn.CrossEntropyLoss(ignore_index=0)

# Step 7: Starting training
num_epochs = 10
print("Step 7: Starting training...")
for epoch in range(num_epochs):
    print(f"Epoch {epoch + 1}/{num_epochs}")
    model.train()
    total_loss = 0
    batch_count = 0

    for src, tgt in dataloader:
        batch_count += 1
        print(f"Processing batch {batch_count}/{len(dataloader)}...", end='\r')
        src, tgt = src.to(device), tgt.to(device)
        tgt_input = tgt[:, :-1]
        tgt_output = tgt[:, 1:]
        
        output = model(src, tgt_input)
        
        output = output.view(-1, len(tgt_vocab))
        tgt_output = tgt_output.contiguous().view(-1)
        
        loss = criterion(output, tgt_output)
        
        optimizer.zero_grad()
        loss.backward() 
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch + 1} completed, Average Loss: {avg_loss:.4f}")

print("Step 8: Saving the model...")
torch.save(model.state_dict(), 'model_weights.pth')
print("Model training complete and saved to 'model_weights.pth'.")
