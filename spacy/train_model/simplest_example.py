"""
This is the simplest example of training NER (named entity recognizer).
NER is responsible for recognizing "Apple" as a 'company', "George Bush" as a 'person', and so on.
THE GOAL for training model is to recognize in text 'iPhone' as a 'GADGET' (for example), and so on.
How do we learn the model to recognizing specific words in specific context?
Through showing to model a few hundreds of examples. Where we showing exactly word position and we label what it is.
For example in text 'Who is Shaka Khan?' we can label like this: {"entities": [(7, 17, "PERSON")]}
or
'I like London and Berlin.' And here: {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]})

we are using tuple with text and dict inside.
"""


import plac
import random
import warnings
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding


# training data
TRAIN_DATA = [

    # EXAMPLES
    #("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
    #("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),

    # MY TRAINING DATA
    ("I like to work with python. Python is my favourite programming language :)", {"entities": [(20, 26, "P-LANG"), (28, 34, "P-LANG")]}),
    ("If you are someday in the zoo, you probably can see a python snake", {"entities": [(54, 60, "ANIMAL")]}),
    ("Do you like pythons?", {"entities": [(12, 19, "ANIMAL")]}),
    ("Do you like python?", {"entities": [(12, 18, "P-LANG")]}),
    ("Pythons are ver long", {"entities": [(0, 7, "ANIMAL")]}),
]

'''
Spacy should detect and label words depending on the context.
In sentence "I like to work with python" - spacy should labeled python as PROGRAMMING LANGUAGE
But in sentence "Python is my favourite animal" - spacy should labeled python as ANIMAL
'''
# This is the result for 100 iterations
# [('python', 'P-LANG'), ('animal', 'P-LANG'), ('Besides', 'P-LANG'), ('python', 'P-LANG')]
# This is the result for 1000 iterations
# [('python', 'P-LANG'), ('Besides', 'P-LANG')]
# Conclusion? Amount of training_data is more important than the number of iterations.
# Co to właściwie jest ta ilość iteracji? Porównać to z tutkiem... (teraz)
# TODO na prezentacji pokazac przyklady dla n_iter:
#  10-nic nie znajduje,
#  50-znajduje ale zle, za duzo,
#  100-znajduje super!
def main(model=None, output_dir=None, n_iter=1000):
    """Load the model, set up the pipeline and train the entity recognizer."""

    # Create blank Language class
    nlp = spacy.blank("en")

    # Create the built-in pipeline components and add them to the pipeline
    # Get it so we can add labels
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)

    # Add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    # only train NER
    with nlp.disable_pipes(*other_pipes), warnings.catch_warnings():
        # show warnings for misaligned entity spans once
        warnings.filterwarnings("once", category=UserWarning, module='spacy')

        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print("Losses", losses)

    # TEST THE TRAINED MODEL
    print('\nSo what are we detected?:')

    # Manually test. Try with text, what wont be used in train data!
    doc = nlp("I like snakes and other animals. Byt python is my favourive animal. Besides, I like to work with python programming language.")
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents]) # Should mark first 'python' as a ANIMAL and second 'python' as a P-LANG

    # auto - from text's from our train data
    #for text, _ in TRAIN_DATA:
        #doc = nlp(text)
        #print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
        ##print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        for text, _ in TRAIN_DATA:
            doc = nlp2(text)
            print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
            print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])


if __name__ == "__main__":
    plac.call(main)

    # Expected output:
    # Entities [('Shaka Khan', 'PERSON')]
    # Tokens [('Who', '', 2), ('is', '', 2), ('Shaka', 'PERSON', 3),
    # ('Khan', 'PERSON', 1), ('?', '', 2)]
    # Entities [('London', 'LOC'), ('Berlin', 'LOC')]
    # Tokens [('I', '', 2), ('like', '', 2), ('London', 'LOC', 3),
    # ('and', '', 2), ('Berlin', 'LOC', 3), ('.', '', 2)]