"""
Spacy is simply for text recognition.
This is the simplest spacy example.
"""

import spacy

# Load model (previously installed model by command: python3 -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Create document through our model
doc = nlp("Apple is my favourite company")

# Receive results!
print(f'''
    This shows us first token: {doc[0]}
    This shows us recognized by model first entity and what it was labelled: {doc.ents[0].text} - {doc.ents[0].label_}
''')