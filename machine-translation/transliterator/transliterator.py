# mapping for Hindi to Telugu
hindi_to_telugu_map = {
    'अ': 'అ', 'आ': 'ఆ', 'इ': 'ఇ', 'ई': 'ఈ', 'उ': 'ఉ', 'ऊ': 'ఊ', 'ऋ': 'ృ', 'ए': 'ఎ', 'ऐ': 'ఐ', 
    'ओ': 'ఓ', 'औ': 'ఔ', 'अं': 'ం', 'अः': 'ః', 'क': 'క', 'ख': 'ఖ', 'ग': 'గ', 'घ': 'ఘ', 'च': 'చ', 
    'छ': 'ఛ', 'ज': 'జ', 'झ': 'ఝ', 'ट': 'ట', 'ठ': 'థ', 'ड': 'డ', 'ढ': 'ఢ', 'ण': 'ణ', 'त': 'త', 
    'थ': 'థ', 'द': 'ద', 'ध': 'ధ', 'न': 'న', 'प': 'ప', 'फ': 'ఫ', 'ब': 'బ', 'भ': 'భ', 'म': 'మ', 
    'य': 'య', 'र': 'ర', 'ल': 'ల', 'व': 'వ', 'श': 'శ', 'ष': 'ష', 'स': 'స', 'ह': 'హ', 'क्ष': 'క్ష', 
    'त्र': 'త్ర', 'ज्ञ': 'జ్ఞ', 'ा': 'ా', 'ि': 'ి', 'ी': 'ీ', 'ु': 'ు', 'ू': 'ూ', 'े': 'ే', 'ै': 'ై', 
    'ो': 'ో', 'ौ': 'ౌ', 'ं   ': 'ం', 'ः': 'ః', '।': '.', '॥': '.'
}

def hindi_to_telugu_transliterate(hindi_text):
    telugu_text = ""
    
    for char in hindi_text:
        if char in hindi_to_telugu_map:
            telugu_text += hindi_to_telugu_map[char]
        else:
            telugu_text += char
            
    return telugu_text

# testing script
hindi_text = "भारत"
telugu_text = hindi_to_telugu_transliterate(hindi_text)
print(f"Hindi: {hindi_text}")
print(f"Telugu: {telugu_text}")
