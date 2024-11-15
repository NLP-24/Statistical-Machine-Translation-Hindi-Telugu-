import re

# List of Hindi stopwords
stopwords = [
    "मैं", "मुझको", "मेरा", "अपने आप को", "हमने", "हमारा", "अपना", "हम", "आप", "आपका",
    "तुम्हारा", "अपने आप", "स्वयं", "वह", "इसे", "उसके", "खुद को", "कि वह", "उसकी", 
    "उसका", "खुद ही", "यह", "इसके", "उन्होने", "अपने", "क्या", "जो", "किसे", "किसको", 
    "कि", "ये", "हूँ", "होता है", "रहे", "थी", "थे", "होना", "गया", "किया जा रहा है", 
    "किया है", "है", "पडा", "होने", "करना", "करता है", "किया", "रही", "एक", "लेकिन", 
    "अगर", "या", "क्यूंकि", "जैसा", "जब तक", "जबकि", "की", "पर", "द्वारा", "के लिए", 
    "साथ", "के बारे में", "खिलाफ", "बीच", "में", "के माध्यम से", "दौरान", "से पहले", 
    "के बाद", "ऊपर", "नीचे", "को", "से", "तक", "से नीचे", "करने में", "निकल", "बंद", 
    "से अधिक", "तहत", "दुबारा", "आगे", "फिर", "एक बार", "यहाँ", "वहाँ", "कब", "कहाँ", 
    "क्यों", "कैसे", "सारे", "किसी", "दोनो", "प्रत्येक", "ज्यादा", "अधिकांश", "अन्य", 
    "में कुछ", "ऐसा", "में कोई", "मात्र", "खुद", "समान", "इसलिए", "बहुत", "सकता", 
    "जायेंगे", "जरा", "चाहिए", "अभी", "और", "कर दिया", "रखें", "का", "हैं", "इस", 
    "होता", "करने", "ने", "बनी", "तो", "ही", "हो", "इसका", "था", "हुआ", "वाले", "बाद", 
    "लिए", "सकते", "इसमें", "दो", "वे", "करते", "कहा", "वर्ग", "कई", "करें", "होती", 
    "अपनी", "उनके", "यदि", "हुई", "जा", "कहते", "जब", "होते", "कोई", "हुए", "व", 
    "जैसे", "सभी", "करता", "उनकी", "तरह", "उस", "आदि", "इसकी", "उनका", "इसी", "पे", 
    "तथा", "भी", "परंतु", "इन", "कम", "दूर", "पूरे", "गये", "तुम", "मै", "यहां", "हुये", 
    "कभी", "अथवा", "गयी", "प्रति", "जाता", "इन्हें", "गई", "अब", "जिसमें", "लिया", 
    "बड़ा", "जाती", "तब", "उसे", "जाते", "लेकर", "बड़े", "दूसरे", "जाने", "बाहर", 
    "स्थान", "उन्हें", "गए", "ऐसे", "जिससे", "समय", "दोनों", "किए", "रहती", "इनके", 
    "इनका", "इनकी", "सकती", "आज", "कल", "जिन्हें", "जिन्हों", "तिन्हें", "तिन्हों", 
    "किन्हों", "किन्हें", "इत्यादि", "इन्हों", "उन्हों", "बिलकुल", "निहायत", "इन्हीं", 
    "उन्हीं", "जितना", "दूसरा", "कितना", "साबुत", "वग़ैरह", "कौनसा", "लिये", "दिया", 
    "जिसे", "तिसे", "काफ़ी", "पहले", "बाला", "मानो", "अंदर", "भीतर", "पूरा", "सारा", 
    "उनको", "वहीं", "जहाँ", "जीधर", "﻿के", "एवं", "कुछ", "कुल", "रहा", "जिस", "जिन", 
    "तिस", "तिन", "कौन", "किस", "संग", "यही", "बही", "उसी", "मगर", "कर", "मे", "एस", 
    "उन", "सो", "अत"
]


# Sample Hindi-Telugu corpus
hindi_sentences = [
    "मैं तेलुगु सीख रहा हूँ।",
    "हमारा भारत महान है।",
    "आपका दिन शुभ हो।"
]

telugu_sentences = [
    "నేను తెలుగు నేర్చుకుంటున్నాను.",
    "మన భారత్ గొప్పది.",
    "మీ రోజు శుభమయం కావాలి."
]

# Function to preprocess Hindi text
def preprocess(text, stopwords):
    # Tokenize the sentence
    words = text.split()
    
    # Identify stopwords and mark them (optional)
    processed_words = []
    for word in words:
        if word in stopwords:
            processed_words.append(f"<STOP>{word}<STOP>")  # Optional marker for stopwords
        else:
            processed_words.append(word)
    
    return " ".join(processed_words)

# Preprocess the Hindi corpus
preprocessed_hindi = [preprocess(sentence, stopwords) for sentence in hindi_sentences]

# Display the processed Hindi corpus
print("Preprocessed Hindi Sentences:")
for sentence in preprocessed_hindi:
    print(sentence)

# Optional: Pair Hindi-Telugu corpus
training_pairs = list(zip(preprocessed_hindi, telugu_sentences))

print("\nTraining Pairs:")
for pair in training_pairs:
    print(pair)

# Step for Model Training (e.g., using seq2seq model)
# 1. Tokenize the sentences.
# 2. Create embeddings for words (including stopwords).
# 3. Train a model on (Hindi -> Telugu) pairs.

# Post-processing for translation output (reverse marker logic if added)
def postprocess(translated_text):
    # Remove stopword markers if any
    return re.sub(r"<STOP>(.*?)<STOP>", r"\1", translated_text)

# Example usage of postprocess
example_output = "నేను <STOP>తెలుగు<STOP> నేర్చుకుంటున్నాను."
print("\nPostprocessed Translation Output:")
print(postprocess(example_output))
