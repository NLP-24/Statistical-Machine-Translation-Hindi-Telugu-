# List of common Hindi suffixes
suffixes = [
    "अक", "अनीय", "आ", "आई", "आबाद", "आर", "आस", "इया", "ई", 
    "कार", "खोर", "गर", "ची", "दार", "पा", "बाज", "वाला", 
    "शाली", "हरा", "हीन"
]

def preprocess(text):
    return text.strip()

def identify_suffix_words(text, suffixes):
    text = preprocess(text)
    words = text.split()
    words_with_suffix = []

    for word in words:
        for suffix in suffixes:
            if word.endswith(suffix):
                words_with_suffix.append(word)
                break  
    
    return words_with_suffix

text = "भारत एक आबाद देश है और इसकी संस्कृति अत्यधिक शाली है।"

identified_words = identify_suffix_words(text, suffixes)

print("Words with specified suffixes:")
print(identified_words)
