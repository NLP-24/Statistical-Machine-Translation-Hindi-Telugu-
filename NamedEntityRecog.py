# List of common Hindi suffixes
suffixes = [
    "अक", "अनीय", "आ", "आई", "आबाद", "आर", "आस", "इया", "ई", 
    "कार", "खोर", "गर", "ची", "दार", "पा", "बाज", "वाला", 
    "शाली", "हरा", "हीन"
]

# Sample Hindi text
text = "भारत एक आबाद देश है और इसकी संस्कृति अत्यधिक शाली है।"

# Function to preprocess text (optional, expand as needed)
def preprocess(text):
    # Normalize whitespace, lowercase, etc., if needed
    return text.strip()

# Function to identify words with specific suffixes
def identify_suffix_words(text, suffixes):
    text = preprocess(text)
    words = text.split()
    words_with_suffix = []

    for word in words:
        for suffix in suffixes:
            if word.endswith(suffix):
                words_with_suffix.append(word)
                break  # Stop checking other suffixes for this word
    
    return words_with_suffix

# Identify words with the specified suffixes
identified_words = identify_suffix_words(text, suffixes)

print("Words with specified suffixes:")
print(identified_words)
