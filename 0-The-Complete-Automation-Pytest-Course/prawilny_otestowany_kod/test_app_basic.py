def add(*args):
    return sum(args)


def test_add():
    assert add(1, 2) == 3
