def load_data(file_path):
    src_sentences, tgt_sentences = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            src, tgt = line.strip().split('\t')
            src_sentences.append(src)
            tgt_sentences.append(tgt)
    return src_sentences, tgt_sentences
