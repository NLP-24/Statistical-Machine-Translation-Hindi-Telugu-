import torch
import torch.nn as nn
from torch.nn import Transformer

class TransformerModel(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, embed_size=256, num_heads=8, num_layers=6):
        super(TransformerModel, self).__init__()
        self.encoder_embedding = nn.Embedding(src_vocab_size, embed_size)
        self.decoder_embedding = nn.Embedding(tgt_vocab_size, embed_size)
        self.transformer = Transformer(d_model=embed_size, nhead=num_heads, num_encoder_layers=num_layers,
                                       num_decoder_layers=num_layers, batch_first=True)
        self.fc_out = nn.Linear(embed_size, tgt_vocab_size)

    def forward(self, src, tgt):
        src_embed = self.encoder_embedding(src)
        tgt_embed = self.decoder_embedding(tgt)
        tgt_mask = self.generate_square_subsequent_mask(tgt.size(1)).to(src.device)
        out = self.transformer(src_embed, tgt_embed, tgt_mask=tgt_mask)
        out = self.fc_out(out)
        return out

    def generate_square_subsequent_mask(self, size):
        return torch.triu(torch.ones(size, size), diagonal=1).bool()
