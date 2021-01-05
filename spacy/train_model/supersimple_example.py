"""
Let’s write a simple training loop from scratch! (from spacy beginner tutorial).
"""

import spacy
import random

TRAINING_DATA = [
    ("Pythons are very long", {"entities": [(0, 7, "ANIMAL")]}),
    ("Do you see that python?", {"entities": [(16, 22, "ANIMAL")]}),
    ("Lions lie on the street", {"entities": []}),
    ("I like pythons.", {"entities": [(7, 14, "ANIMAL")]}),
    ("I like to program in python language.", {"entities": [(21, 27, "PROGRAMMING-LANGUAGE")]}),
    ("Do you like to program in python?", {"entities": [(26, 32, "PROGRAMMING-LANGUAGE")]}),
    ("Python is the one of the best computer programming language.", {"entities": [(0, 6, "PROGRAMMING-LANGUAGE")]}),
    ("I like to program in javascript.", {"entities": []}),
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
doc = nlp("I like to watch Pythons in zoo. Besides, I like to program in python.")
# Pythons - ANIMAL
# python - PROGRAMMIG-LANGUAGE
for entity in doc.ents:
    print(f'{entity.text} - {entity.label_}')
