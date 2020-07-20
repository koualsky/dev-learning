"""
How to implement iterator? Just define __getitem__ function
"""


class Sentence:

    def __init__(self, text):
        self.text = text
        # self.text = text.split() # odkomentuj a zobaczysz co sie stanie

    def __getitem__(self, index):
        return self.text[index]


s = Sentence('Hello World')
for e in s:
    print(e)
