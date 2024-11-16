import spacy
import requests

# Load the spaCy model for NER
nlp = spacy.load("model.pth")  # Multilingual model for NER

def link_entity_to_wikipedia(entity):
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={entity}&limit=1&namespace=0&format=json"
    response = requests.get(url)
    data = response.json()
    if data[1]:
        return data[3][0]  # Return the first URL
    return None

def perform_nel(sentence):
    doc = nlp(sentence)
    linked_entities = []
    for ent in doc.ents:
        wiki_link = link_entity_to_wikipedia(ent.text)
        if wiki_link:
            linked_entities.append((ent.text, ent.label_, wiki_link))
    return linked_entities

def apply_nel_to_dataset(sentences):
    processed_sentences = []
    for sentence in sentences:
        linked_entities = perform_nel(sentence)
        # Format the linked entities as a string
        linked_entities_str = "; ".join([f"{text} ({label}) [{link}]" for text, label, link in linked_entities])
        processed_sentences.append(linked_entities_str)
    return processed_sentences



# Usage :-
# pip install spacy requests
# python -m spacy download xx_ent_wiki_sm