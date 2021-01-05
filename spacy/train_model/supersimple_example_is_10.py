"""
Let’s write a simple training loop from scratch! (from spacy beginner tutorial).
"""

import spacy
import random

TRAINING_DATA = [
    ("A patient, Sebastian de la Cruz, born 11/07/1972", {"entities": [(11, 31, "PERSON")]}),
    ("A patient, Sebastian de la Cruz, ", {"entities": [(11, 31, "PERSON")]}),
    ("A patient, Sebastian de la Cruz, born 11/07/1972", {"entities": [(38, 48, "DATE OF BIRTH")]}),
    ("patient, Sebastian Bush, born 07/19/1987", {"entities": [(30, 40, "DATE OF BIRTH")]}),
    ("emergency contact can be reached at +44 7913 234431", {"entities": [(36, 51, "TELEPHONE NUMBER")]}),
    ("contact can be reached at +44 6713 434341", {"entities": [(26, 41, "TELEPHONE NUMBER")]}),
    ("He came into the hospital with his passport 2328 23408 that has been stored with his belongings", {"entities": [(44, 54, "PASSPORT NUMBER")]}),
    ("came into the hospital with his passport 9711 23181 that has been stored with his belongings", {"entities": [(41, 51, "PASSPORT NUMBER")]}),
    ("took some wonky medicine 9086785 that didn't go down so well.", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("some wonky medicine 9086785 that didn't go down so well.", {"entities": [(20, 27, "IDENTIFIER")]}),
]

# Blank English model, blank entity recognizer, add it to the pipeline, add a new label
nlp = spacy.blank('en')
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

# Add labels
# 1. manually
#ner.add_label('ANIMAL')
#ner.add_label('P-LENG')
# 2. automatically
for _, annotations in TRAINING_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Start the training
nlp.begin_training()

# Train for 10 iterations
for itn in range(10):
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Divide TRAINING_DATA into batches
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Update the model
        nlp.update(texts, annotations, losses=losses)
        #print(losses)

# Does the model recognize new entity labels in the given text?
doc = nlp("""A patient, Sebastian de la Cruz, born 11/07/1972, 
took some wonky medicine 9086785 that didn't go down so well. 
He was admitted to the ER and his emergency contact can be reached 
at +44 7913 234431 or 01202 789456 if they are at home. He came 
into the hospital with his passport 2788 23418 that has been 
stored with his belongings.""")
for entity in doc.ents:
    print(f'{entity.text} - {entity.label_}')
