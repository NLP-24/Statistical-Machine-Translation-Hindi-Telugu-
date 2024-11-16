# Expanded suffix patterns for both Hindi and Telugu POS tagging
suffix_dict = {
    'noun': {
        'hindi': ['ता', 'त्व', 'क', 'जी', 'र', 'आन', 'पन', 'वाला', 'कारी', 'वा', 'ई', 'ी', 'े', 'ि', 'ा', 'याँ', 'ओं', 
                  'ए', 'औं', 'यों', 'त्व', 'जन', 'धारी', 'धार', 'प्रदेश', 'वाले', 'इक', 'शासन', 'स्थान', 'माल', 'खण्ड',
                  'प्रमुख', 'कर्म', 'योजना', 'वर्ग', 'समाज', 'पुरुष', 'महिला'],
        'telugu': ['అయ్య', 'య్య', 'కుమారి', 'భాష', 'రాజు', 'వారి', 'అల్లు', 'తన', 'మీ', 'ఇన', 'ఇసి', 'ము', 'మా', 'శాస్త్ర',
                   'పనితీరు', 'ప్రభుత్వం', 'కోసం', 'ప్రపంచం', 'వారు', 'పురుష', 'మహిళ', 'సంస్థ', 'విభాగం', 'నగరం', 'ఇంజనీర్']
    },
    'verb': {
        'hindi': ['ना', 'ता', 'ती', 'ते', 'ए', 'ा', 'ओ', 'इए', 'कर', 'गा', 'गी', 'गे', 'ऊँ', 'ता', 'ते', 'ती', 'करना', 
                  'रहा', 'रही', 'रहे', 'सकना', 'चलना', 'बैठना', 'जाना', 'उठाना', 'सिखाना', 'पहुंचाना', 'देखना', 'बोलना'],
        'telugu': ['డా', 'అయ్య', 'తే', 'డిగ', 'తారు', 'చేసే', 'బోతుంది', 'అది', 'చేయు', 'పెట్టింది', 'పరిశీలించు', 'పోయారు',
                   'పరిగెత్తు', 'పరచు', 'బెట్టి', 'చూడు']
    },
    'adjective': {
        'hindi': ['ा', 'ी', 'े', 'वाला', 'ीला', 'ुआ', 'ीन', 'ही', 'रा', 'री', 'रे', 'दार', 'णीय', 'कृत', 'गत', 'शाली', 
                  'पूर्ण', 'उच्च', 'महान', 'स्वस्थ', 'सामाजिक', 'नया', 'पुराना', 'अच्छा', 'बुरा', 'सुंदर', 'साधारण'],
        'telugu': ['చెప్పే', 'అల్లు', 'పొడి', 'సరే', 'విపరీతమైన', 'పుష్ప', 'నయం', 'శుభ్రమైన', 'అద్భుతమైన', 'ప్రముఖ', 'బలమైన',
                   'ఆకర్షణీయమైన', 'చిరునవ్వు']
    },
    'adverb': {
        'hindi': ['से', 'में', 'पर', 'ही', 'भी', 'कर', 'ना', 'तर', 'बाहर', 'वहाँ', 'यहाँ', 'जैसे', 'कैसे', 'जहाँ', 
                  'तभी', 'पहले', 'हालांकि', 'नहीं', 'अब', 'सिर्फ', 'फिर', 'जरा', 'यहीं'],
        'telugu': ['మీది', 'పక్క', 'ఉంచు', 'పరిగెత్తు', 'పెరుగుతుంది', 'నేటి', 'సమయంలో', 'ఇప్పుడు', 'తప్పక']
    },
    'pronoun': {
        'hindi': ['मैं', 'तुम', 'वह', 'वे', 'ये', 'यह', 'जो', 'कौन', 'क्या', 'उस', 'इस', 'तुम्हारा', 'हम', 'तुम्हें', 
                  'मुझसे', 'तुम्हारे', 'आप', 'इन्हें', 'आपका', 'यहाँ', 'वहाँ'],
        'telugu': ['నేను', 'నీవు', 'అతను', 'ఆమె', 'మేము', 'మీకో', 'మేము', 'ఆది', 'అవి', 'నేను', 'మీరు', 'అతడూ']
    },
    'conjunction': {
        'hindi': ['और', 'लेकिन', 'जबकि', 'यदि', 'परंतु', 'किंतु', 'तथा', 'या', 'तो', 'नहीं', 'चाहे', 'अथवा', 'इसलिए', 
                  'क्योंकि', 'हालांकि', 'तब', 'जैसा कि'],
        'telugu': ['మరియు', 'కానీ', 'ఇది', 'అందువల్ల', 'కానీ', 'అయితే', 'ఇంకా', 'మరి']
    },
    'preposition': {
        'hindi': ['में', 'से', 'पर', 'को', 'तक', 'के', 'लिए', 'द्वारा', 'साथ', 'बिना', 'ऊपर', 'नीचे', 'बीच', 'आगे', 
                  'पास', 'नज़दीक', 'अंदर', 'सामने', 'बगल'],
        'telugu': ['లో', 'మీకు', 'ముందు', 'ఆధారంగా', 'నుండి', 'ప్రత్యేకంగా', 'పైన', 'కింద', 'పక్క']
    },
    'interjection': {
        'hindi': ['वाह', 'अरे', 'ओह', 'अहा', 'उफ़', 'हाय', 'ओ', 'आह', 'शाबाश', 'अरे', 'ओये', 'अच्छा', 'अलविदा', 
                  'सुप्रभात', 'धन्यवाद', 'माफी'],
        'telugu': ['అయ్యో', 'ఆహా', 'ఓహ్', 'ఉహ్', 'ఆహ', 'అదృష్టం']
    }
}

# Expanded common words dictionary for both Hindi and Telugu with predefined POS tags
common_words = {
    'hindi': {
        'है': 'verb', 'हूँ': 'verb', 'हो': 'verb', 'हैं': 'verb', 'थी': 'verb',
        'था': 'verb', 'थे': 'verb', 'होगा': 'verb', 'गया': 'verb', 'आई': 'verb',
        'का': 'preposition', 'की': 'preposition', 'के': 'preposition', 
        'यह': 'pronoun', 'वह': 'pronoun', 'जो': 'pronoun', 'कौन': 'pronoun',
        'और': 'conjunction', 'लेकिन': 'conjunction', 'परंतु': 'conjunction',
        'से': 'preposition', 'तक': 'preposition', 'में': 'preposition',
        'भारत': 'proper_noun', 'दिल्ली': 'proper_noun', 'मुंबई': 'proper_noun', 
        'राम': 'proper_noun', 'सीता': 'proper_noun', 'मनुष्य': 'noun', 'देश': 'noun',
        'बहुत': 'adverb', 'ही': 'adverb', 'सभी': 'pronoun'
    },
    'telugu': {
        'ఇది': 'verb', 'నేను': 'pronoun', 'అతను': 'pronoun', 'మేము': 'pronoun',
        'మరియు': 'conjunction', 'కానీ': 'conjunction', 'తప్ప': 'verb',
        'నిమితం': 'preposition', 'ఈ': 'adjective', 'అవసరం': 'noun', 
        'తెలుగు': 'proper_noun', 'పర్యటన': 'noun', 'సోషల్': 'adjective', 
        'బాగుంది': 'verb', 'అవకాశం': 'noun', 'మీరు': 'pronoun'
    }
}

def is_proper_noun(word, language):
    return word in common_words[language] and common_words[language][word] == 'proper_noun'

def pos_tag(word, previous_word=None, language='hindi'):
    if word in common_words[language]:
        return common_words[language][word]

    if is_proper_noun(word, language):
        return 'proper_noun'

    for pos, suffixes in suffix_dict.items():
        for suffix in suffixes[language]:
            if word.endswith(suffix):
                return pos
    
    if language == 'hindi':
        if previous_word in ['का', 'की', 'के']:
            if word.endswith('ा'):
                return 'adjective'
            
    elif language == 'telugu':
        if previous_word in ['అంటే', 'పాటు']:
            if word.endswith('లు'):
                return 'noun'

    return 'noun'

def process_sentence(sentence, language='hindi'):
    words = sentence.split()
    tagged_words = []
    
    for i, word in enumerate(words):
        if i == 0:
            tagged_words.append((word, pos_tag(word, language=language)))
        else:
            tagged_words.append((word, pos_tag(word, previous_word=words[i-1], language=language)))
    
    return tagged_words

#test sentences
test_sentence_hindi = "राम दिल्ली गया और सीता घर पर थी"
test_sentence_telugu = "నేను స్కూలుకు వెళ్లాను మరియు అతను కూడా వెళ్లాడు"

print("Hindi Sentence POS Tags:")
for word, pos in process_sentence(test_sentence_hindi, language='hindi'):
    print(f"{word}: {pos}")

print("\nTelugu Sentence POS Tags:")
for word, pos in process_sentence(test_sentence_telugu, language='telugu'):
    print(f"{word}: {pos}")
