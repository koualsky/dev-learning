import pytest
from program import inc

def test_inc_3():
    assert inc(3) != 5

def test_inc_8():
    assert inc(7) == 8

def test_inc_0():
    assert inc(0) == 1


# Go to this directory and type: pytest test.py