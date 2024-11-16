def generate_ngrams(sentence, n):

    tokens = sentence.split()
    ngrams = [' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams

def preprocess_data(data, n=2):

    preprocessed_data = []
    
    for pair in data:
        hindi_text = pair['hindi']
        telugu_text = pair['telugu']
        
        hindi_ngrams = generate_ngrams(hindi_text, n)
        telugu_ngrams = generate_ngrams(telugu_text, n)
        
        preprocessed_data.append({
            "hindi_text": hindi_text,
            "telugu_text": telugu_text,
            "hindi_ngrams": hindi_ngrams,
            "telugu_ngrams": telugu_ngrams
        })
    
    return preprocessed_data

# Example data to test the script
data = [
    {"hindi": "यह एक हिंदी वाक्य है", "telugu": "ఇది ఒక హిందీ వాక్యం"},
    {"hindi": "मैं घर जा रहा हूँ", "telugu": "నేను ఇంటికి వెళ్తున్నాను"},
    {"hindi": "कृपया ध्यान दें", "telugu": "దయచేసి గమనించండి"},
]

n = 2  
processed = preprocess_data(data, n)

for entry in processed:
    print("Original Hindi Text:", entry['hindi_text'])
    print("Original Telugu Text:", entry['telugu_text'])
    print("Hindi Bigrams:", entry['hindi_ngrams'])
    print("Telugu Bigrams:", entry['telugu_ngrams'])
    print("-" * 30)
