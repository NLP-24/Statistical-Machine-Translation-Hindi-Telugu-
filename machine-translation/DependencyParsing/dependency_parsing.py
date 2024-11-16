import spacy

nlp = spacy.load("./model.pth")

def perform_dependency_parsing(sentence):
    doc = nlp(sentence)
    parsed_sentence = []
    for token in doc:
        parsed_sentence.append((token.text, token.dep_, token.head.text))
    return parsed_sentence

def apply_dependency_parsing_to_dataset(sentences):
    parsed_sentences = []
    for sentence in sentences:
        parsed_sentence = perform_dependency_parsing(sentence)
      
        parsed_sentence_str = "; ".join([f"{word} ({dep}) -> {head}" for word, dep, head in parsed_sentence])
        parsed_sentences.append(parsed_sentence_str)
    return parsed_sentences


# Usage :-
# pip install spacy
# python -m spacy download en_core_web_sm