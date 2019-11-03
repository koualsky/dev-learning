# *args
def hula(*argv):
    for e in argv:
        print(e)


hula(1, 2, 3)

# **kwargs


def dula(**kwargs):
    for key, value in kwargs.items():
        print('{} == {}'.format(key, value))


dula(first='Geeks', mid='for')

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
dula(**kwargs)