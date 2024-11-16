import torch
from testing.models.transformer_model import TransformerModel
from vocab import Vocab
from sklearn.metrics import precision_score

src_vocab = Vocab.load('machine-translation\\vocab\\src_vocab.pkl')
tgt_vocab = Vocab.load('machine-translation\\vocab\\tgt_vocab.pkl')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = TransformerModel(len(src_vocab), len(tgt_vocab)).to(device)

model.load_state_dict(torch.load('testing\\checkpoints\\model.pth', map_location=device))
model.eval()

def translate_sentence(sentence):
    src_tensor = torch.tensor([1] + src_vocab.encode(sentence) + [2]).unsqueeze(0).to(device)
    output = model(src_tensor, torch.tensor([[1]]).to(device))
    translated = tgt_vocab.decode(torch.argmax(output, dim=-1).squeeze().tolist())
    return translated

def compute_metrics(src_sentences, tgt_sentences):
    correct_predictions = 0
    total_predictions = 0
    all_predicted_words = []
    all_true_words = []

    for src, tgt in zip(src_sentences, tgt_sentences):
        predicted_translation = translate_sentence(src)
        true_translation = tgt

        pred_words = predicted_translation.split()
        true_words = true_translation.split()

        all_predicted_words.extend(pred_words)
        all_true_words.extend(true_words)

        if predicted_translation == true_translation:
            correct_predictions += 1
        total_predictions += 1

    precision = precision_score(all_true_words, all_predicted_words, average='binary', pos_label='1')

    accuracy = correct_predictions / total_predictions
    return accuracy, precision

src_sentences = ["मुझे काम करना है", "यह एक अच्छा दिन है"]
tgt_sentences = ["I have to work", "It is a nice day"]

accuracy, precision = compute_metrics(src_sentences, tgt_sentences)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
