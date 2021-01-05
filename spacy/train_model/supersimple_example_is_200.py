"""
Let’s write a simple training loop from scratch! (from spacy beginner tutorial).
"""

import spacy
import random

TRAINING_DATA = [
    ("A patient, Sebastian de la Cruz, born 11/07/1972", {"entities": [(11, 31, "PERSON")]}),
    ("A patient, Sebastian de la Cruz, ", {"entities": [(11, 31, "PERSON")]}),
    ("A patient, Sebastian de la Cruz,", {"entities": [(11, 31, "PERSON")]}),
    ("A patient, Sebastian de la Cruz", {"entities": [(11, 31, "PERSON")]}),
    ("patient, Sebastian de la Cruz", {"entities": [(9, 29, "PERSON")]}),
    (", Sebastian de la Cruz", {"entities": [(2, 22, "PERSON")]}),
    ("Sebastian de la Cruz", {"entities": [(0, 20, "PERSON")]}),
    ("A patient John Doe, born 2/11/1990", {"entities": [(10, 18, "PERSON")]}),
    ("A patient, John Doe, ", {"entities": [(11, 39, "PERSON")]}),
    ("A patient John Doe", {"entities": [(10, 18, "PERSON")]}),
    ("patient John Doe", {"entities": [(8, 16, "PERSON")]}),
    ("John Doe", {"entities": [(0, 8, "PERSON")]}),
    ("John Deer", {"entities": [(0, 9, "PERSON")]}),
    ("Jennifer Aniston", {"entities": [(0, 16, "PERSON")]}),
    ("Mr Jean Claude van Damme", {"entities": [(0, 24, "PERSON")]}),
    ("Jean Claude van Damme", {"entities": [(0, 21, "PERSON")]}),
    ("Mr Bill Gates", {"entities": [(0, 13, "PERSON")]}),
    ("Bill Gates", {"entities": [(0, 10, "PERSON")]}),
    ("Mr Steven Jobs", {"entities": [(0, 14, "PERSON")]}),
    ("A patient, Sebastian de la Cruz, born 11/07/1972", {"entities": [(38, 48, "DATE OF BIRTH")]}),
    ("patient, Sebastian Bush, born 07/19/1987", {"entities": [(30, 40, "DATE OF BIRTH")]}),
    ("born 10/07/1990, took some wonky medicine", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("Sebastian de Santa, born 11/07/1972", {"entities": [(25, 35, "DATE OF BIRTH")]}),
    ("John Travolta, born 11/07/1972", {"entities": [(20, 30, "DATE OF BIRTH")]}),
    (", John Doe, born 11/07/1972, took some wonky medicine", {"entities": [(17, 27, "DATE OF BIRTH")]}),
    ("Johnny Deep, born 01/06/1966, took some wonky medicine", {"entities": [(18, 28, "DATE OF BIRTH")]}),
    ("Ricardo, born 09/02/1953, took some wonky medicine", {"entities": [(14, 24, "DATE OF BIRTH")]}),
    ("Tommy Hilfiger, born 20/12/1985, took some wonky medicine", {"entities": [(21, 31, "DATE OF BIRTH")]}),
    ("Diana Roberos, born 19/10/1995, has a ", {"entities": [(20, 30, "DATE OF BIRTH")]}),
    (", born 19/10/1995, has a ", {"entities": [(7, 17, "DATE OF BIRTH")]}),
    ("born 13/07/1990, has", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("born 20/01/1989,", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("20/01/1989, has a nice bike", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("22/02/1988, has a red car", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("22/02/1988, has a green", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("14/04/1986, has yellow", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("16/06/1985, has", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("17/07/1984, has", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("18/07/1983, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("19/08/1982, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("20/09/1981, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("21/10/1980, ", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("22/11/1979, ", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("23/12/1978,", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("24/01/1977,", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("23/02/1976", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("24/03/1975", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("25/04/1974", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("26/05/1973", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("27/06/1972", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("emergency contact can be reached at +44 7913 234431", {"entities": [(36, 51, "TELEPHONE NUMBER")]}),
    ("contact can be reached at +44 6713 434341", {"entities": [(26, 41, "TELEPHONE NUMBER")]}),
    ("can be reached at +44 6713 434341", {"entities": [(18, 33, "TELEPHONE NUMBER")]}),
    ("at +48 8813 222341", {"entities": [(3, 18, "TELEPHONE NUMBER")]}),
    ("+48 8813 222341", {"entities": [(0, 15, "TELEPHONE NUMBER")]}),
    ("or 01202 789456 if they are at home", {"entities": [(3, 15, "TELEPHONE NUMBER")]}),
    ("10202 675556 if they are at home", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("12345 678900 if they are at", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("98765 432111 if they are", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("10202 555433 if they", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("10101 212126 if", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("22288 777777", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("11111 222222", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("He came into the hospital with his passport 2328 23408 that has been stored with his belongings", {"entities": [(44, 54, "PASSPORT NUMBER")]}),
    ("came into the hospital with his passport 9711 23181 that has been stored with his belongings", {"entities": [(41, 51, "PASSPORT NUMBER")]}),
    ("into the hospital with his passport 2788 23418 that has been stored with his belongings", {"entities": [(36, 46, "PASSPORT NUMBER")]}),
    ("the hospital with his passport 3688 25318 that has been stored with his belongings", {"entities": [(31, 41, "PASSPORT NUMBER")]}),
    ("hospital with his passport 2688 25417 that has been stored with his belongings", {"entities": [(27, 37, "PASSPORT NUMBER")]}),
    ("with his passport 2688 25417 that has been stored with his belongings", {"entities": [(18, 28, "PASSPORT NUMBER")]}),
    ("his passport 2788 23418 that has been stored with his belongings", {"entities": [(13, 23, "PASSPORT NUMBER")]}),
    ("He came into the hospital with his passport 3439 34518 that has been stored with his", {"entities": [(44, 54, "PASSPORT NUMBER")]}),
    ("came into the hospital with his passport 9711 23181 that has been stored with", {"entities": [(41, 51, "PASSPORT NUMBER")]}),
    ("into the hospital with his passport 1734 63429 that has been stored", {"entities": [(36, 46, "PASSPORT NUMBER")]}),
    ("the hospital with his passport 3788 25418 that has been stored", {"entities": [(31, 41, "PASSPORT NUMBER")]}),
    ("hospital with his passport 3554 24417 that has been", {"entities": [(27, 37, "PASSPORT NUMBER")]}),
    ("with his passport 2689 35417 that has", {"entities": [(18, 28, "PASSPORT NUMBER")]}),
    ("his passport 2768 23428 that", {"entities": [(13, 23, "PASSPORT NUMBER")]}),
    ("passport 2722 11418 that", {"entities": [(9, 19, "PASSPORT NUMBER")]}),
    ("2722 11418 that", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("1234 56789", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("9876 54321", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("1234 54321", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("9876 56789", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("took some wonky medicine 9086785 that didn't go down so well.", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("some wonky medicine 9086785 that didn't go down so well.", {"entities": [(20, 27, "IDENTIFIER")]}),
    ("wonky medicine 9086785 that didn't go down so well.", {"entities": [(15, 22, "IDENTIFIER")]}),
    ("medicine 9086785 that didn't go down so well.", {"entities": [(9, 16, "IDENTIFIER")]}),
    ("9086785 that didn't go down so well.", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785 that didn't go down so", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785 that didn't go down", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785 that didn't go", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785 that didn't", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785 that", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9086785", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("some wonky medicine 9086785 that didn't go down so", {"entities": [(20, 27, "IDENTIFIER")]}),
    ("wonky medicine 9086785 that didn't go down", {"entities": [(15, 22, "IDENTIFIER")]}),
    ("medicine 9086785 that didn't go", {"entities": [(9, 16, "IDENTIFIER")]}),
    ("9086785 that didn't", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("9086785 that", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("9086785", {"entities": [(0, 7, "IDENTIFIER")]}),

    ("A patient, Jean Jarre, born 10/05/1982", {"entities": [(11, 21, "PERSON")]}),
    ("A patient, Jean Jarre, ", {"entities": [(11, 21, "PERSON")]}),
    ("A patient, Jean Jarre,", {"entities": [(11, 21, "PERSON")]}),
    ("A patient, Jean Jarre", {"entities": [(11, 21, "PERSON")]}),
    ("patient, Jean Jarre", {"entities": [(9, 19, "PERSON")]}),
    (", Jean Jarre", {"entities": [(2, 12, "PERSON")]}),
    ("Jean Jarre", {"entities": [(0, 10, "PERSON")]}),
    ("A patient Billy Joe, born 2/11/1990", {"entities": [(10, 19, "PERSON")]}),
    ("A patient, Billy Joe, ", {"entities": [(11, 20, "PERSON")]}),
    ("A patient Billy Joe", {"entities": [(10, 19, "PERSON")]}),
    ("patient Billy Joe", {"entities": [(8, 17, "PERSON")]}),
    ("Billy Joe", {"entities": [(0, 9, "PERSON")]}),
    ("John Deer", {"entities": [(0, 9, "PERSON")]}),
    ("Alicia Keys", {"entities": [(0, 11, "PERSON")]}),
    ("Mr Jack Hack", {"entities": [(0, 12, "PERSON")]}),
    ("Jack Hack", {"entities": [(0, 9, "PERSON")]}),
    ("Mr Billy Goose", {"entities": [(0, 14, "PERSON")]}),
    ("Billy Goose", {"entities": [(0, 11, "PERSON")]}),
    ("Mr Steve Job", {"entities": [(0, 12, "PERSON")]}),
    ("A patient, Sebastian Santa, born 11/07/1963", {"entities": [(33, 43, "DATE OF BIRTH")]}),
    ("patient, Alec Boom, born 07/19/1987", {"entities": [(25, 35, "DATE OF BIRTH")]}),
    ("born 14/03/1993, took some wonky medicine", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("Sebastian, born 06/02/1991", {"entities": [(16, 26, "DATE OF BIRTH")]}),
    ("Johny Deep, born 05/05/1955", {"entities": [(17, 27, "DATE OF BIRTH")]}),
    (", Johny Deep, born 11/07/1972, took some wonky medicine", {"entities": [(19, 29, "DATE OF BIRTH")]}),
    ("John Deeper, born 20/10/1977, took some wonky medicine", {"entities": [(18, 28, "DATE OF BIRTH")]}),
    ("Ricardos Moleros, born 10/03/1949, took some wonky medicine", {"entities": [(23, 33, "DATE OF BIRTH")]}),
    ("Loui Roberts, born 20/12/1985, took some wonky medicine", {"entities": [(19, 29, "DATE OF BIRTH")]}),
    ("Monica Robertos, born 18/11/1985, has a ", {"entities": [(22, 32, "DATE OF BIRTH")]}),
    (", born 14/11/1991, has a ", {"entities": [(7, 17, "DATE OF BIRTH")]}),
    ("born 11/01/1991, has", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("born 21/01/1981,", {"entities": [(5, 15, "DATE OF BIRTH")]}),
    ("21/01/1981, has a nice bike", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("21/02/1981, has a red car", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("23/02/1982, has a green", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("11/01/1986, has yellow", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("11/06/1985, has", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("17/01/1984, has", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("18/07/1983, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("19/01/1982, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("21/09/1981, ha", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("21/11/1981, ", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("20/12/1979, ", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("23/10/1978,", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("23/03/1977,", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("24/04/1976", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("25/01/1975", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("26/07/1974", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("20/08/1973", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("19/09/1972", {"entities": [(0, 10, "DATE OF BIRTH")]}),
    ("emergency contact can be reached at +42 6552 117766", {"entities": [(36, 51, "TELEPHONE NUMBER")]}),
    ("contact can be reached at +41 1234 987654", {"entities": [(26, 41, "TELEPHONE NUMBER")]}),
    ("can be reached at +43 9876 123456", {"entities": [(18, 33, "TELEPHONE NUMBER")]}),
    ("at +48 1234 567890", {"entities": [(3, 18, "TELEPHONE NUMBER")]}),
    ("+48 9876 543210", {"entities": [(0, 15, "TELEPHONE NUMBER")]}),
    ("or 12345 006789 if they are at home", {"entities": [(3, 15, "TELEPHONE NUMBER")]}),
    ("10000 123456 if they are at home", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("20002 987654 if they are at", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("33003 123456 if they are", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("40404 543219 if they", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("55000 116358 if", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("41345 872352", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("26464 098457", {"entities": [(0, 12, "TELEPHONE NUMBER")]}),
    ("He came into the hospital with his passport 2345 29386 that has been stored with his belongings", {"entities": [(44, 54, "PASSPORT NUMBER")]}),
    ("came into the hospital with his passport 9823 83510 that has been stored with his belongings", {"entities": [(41, 51, "PASSPORT NUMBER")]}),
    ("into the hospital with his passport 2324 22358 that has been stored with his belongings", {"entities": [(36, 46, "PASSPORT NUMBER")]}),
    ("the hospital with his passport 1355 25512 that has been stored with his belongings", {"entities": [(31, 41, "PASSPORT NUMBER")]}),
    ("hospital with his passport 4311 22477 that has been stored with his belongings", {"entities": [(27, 37, "PASSPORT NUMBER")]}),
    ("with his passport 2138 25431 that has been stored with his belongings", {"entities": [(18, 28, "PASSPORT NUMBER")]}),
    ("his passport 2758 27745 that has been stored with his belongings", {"entities": [(13, 23, "PASSPORT NUMBER")]}),
    ("He came into the hospital with his passport 7772 31233 that has been stored with his", {"entities": [(44, 54, "PASSPORT NUMBER")]}),
    ("came into the hospital with his passport 9221 26651 that has been stored with", {"entities": [(41, 51, "PASSPORT NUMBER")]}),
    ("into the hospital with his passport 1744 62467 that has been stored", {"entities": [(36, 46, "PASSPORT NUMBER")]}),
    ("the hospital with his passport 3728 67418 that has been stored", {"entities": [(31, 41, "PASSPORT NUMBER")]}),
    ("hospital with his passport 3454 34466 that has been", {"entities": [(27, 37, "PASSPORT NUMBER")]}),
    ("with his passport 2659 33457 that has", {"entities": [(18, 28, "PASSPORT NUMBER")]}),
    ("his passport 2448 24328 that", {"entities": [(13, 23, "PASSPORT NUMBER")]}),
    ("passport 2733 11414 that", {"entities": [(9, 19, "PASSPORT NUMBER")]}),
    ("2725 11448 that", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("1834 56729", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("9886 54351", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("1274 54361", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("9896 56719", {"entities": [(0, 10, "PASSPORT NUMBER")]}),
    ("took some wonky medicine 8906785 that didn't go down so well.", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("some wonky medicine 6546785 that didn't go down so well.", {"entities": [(20, 27, "IDENTIFIER")]}),
    ("wonky medicine 6006785 that didn't go down so well.", {"entities": [(15, 22, "IDENTIFIER")]}),
    ("medicine 3006785 that didn't go down so well.", {"entities": [(9, 16, "IDENTIFIER")]}),
    ("9086000 that didn't go down so well.", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("took some wonky medicine 9000085 that didn't go down so", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9123455 that didn't go down", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9111115 that didn't go", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9085432 that didn't", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 9081824 that", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("took some wonky medicine 4386785", {"entities": [(25, 32, "IDENTIFIER")]}),
    ("some wonky medicine 9022285 that didn't go down so", {"entities": [(20, 27, "IDENTIFIER")]}),
    ("wonky medicine 1286785 that didn't go down", {"entities": [(15, 22, "IDENTIFIER")]}),
    ("medicine 3286785 that didn't go", {"entities": [(9, 16, "IDENTIFIER")]}),
    ("9086744 that didn't", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("9999785 that", {"entities": [(0, 7, "IDENTIFIER")]}),
    ("9121195", {"entities": [(0, 7, "IDENTIFIER")]}),
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
