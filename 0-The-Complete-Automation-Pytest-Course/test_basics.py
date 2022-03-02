""""
pytest
pytest -v                           # with details
pytest -s                           # allows run ipdb inside test
pytest module.py::method            # run specified method
pytest -v tests/services/test_module.py::Class::method  # rus specified method in specified class PLUS extra details (-v)
"""

import os
import pytest
from collections import namedtuple

Task = namedtuple('Task', ['activity', 'name', 'done'])

# 1. Najprostszy test
def test_one():
    assert (1, 2, 3) == (1, 2, 3)


# 2. Fixtury (w teście, bo moga tez byc poza)
@pytest.fixture
def some_dict():
    return {
        'name': 'Damian', 
        'age': '45'
    }

def test_fixturki_elo(some_dict):
    assert some_dict == {
        'name': 'Damian', 
        'age': '45'
    }
 

# Autouse - funkcja udekorowana autouse'm - wykona sie i bedzie to automatycznie w wszystkich testach!
# @pytest.fixture(autouse=True)
# !!!!!!!!!!!!!!!!! nie wiem co to jest i jak to dziala. z opisu wynika ze dziala to jak setUp. ale w takim razie po co by byl setUp? rozkminic to jeszcze


# 4. Parametrize
# Tworzy zmienna 'task' z tym co jest w pierwszej linii listy i robi dla tego wszystkie testy z dekorowanej funkcji.
# Potem powtarza test dla drugiej linii itd...
@pytest.mark.parametrize('task',
                                [
                                    Task('lift', 'x', done=True),
                                    Task('swim', 'james', True),
                                    Task('run', 'JAMES', True),
                                    Task('play', 'JaMeS', False),
                                ]
                            )
def test_three(task):
    assert task == task


@pytest.mark.parametrize('name, age, country',  # comma separated string!
                                [
                                    ('John', 33, 'Ireland'),
                                    ('Jacek', 25, 'Poland'),
                                ]
                            )
def test_three_two(name, age, country):
    assert 'J' in name
    assert age > 24
    assert 'a' in country


tasks_to_try = (
    Task('lift', 'x', done=True),
    Task('swim', 'james', True),
    Task('run', 'JAMES', True),
    Task('play', 'JaMeS', False),
)

@pytest.mark.parametrize('task', tasks_to_try)
def test_four(task):
    assert task == task


@pytest.mark.parametrize('task', tasks_to_try)
class TestOne():
    def test_one(self, task):
        assert task == task


@pytest.mark.smoke  # moge spotkac tego typu custom marki jak smoke czy slow, ale to sa tylko puste dekoratory oznaczajace np ktore testy sa wolne. 
                    # bo pozniej moge sobie to w puszczaniu np pomijac. slabo uzyteczne to raczej.
def test_five():
    pass


# raises errors
def test_some_error():
    with pytest.raises(NameError):
        something.add(1) # i ta funkcja powinna wywalic NameError robiac TA zla operacja bo something nie jest zdefiniowane
                         # albo moge uzyc wczesniej twardo zwracajacej raise...


@pytest.mark.xfail  # pojebane to jest. normalnie test failuje i jest czerwony. a tu daje ten mark i testy przejda normalnie, tylko to bedzie zolte! szatanskie narzedzie...
def test_six():
    ''.append('d')
    # assert 1 == 2



def some_func():
    return 'yello'

# 1 sposob mockowania
# from unittest import mock
# @mock.patch('test_basics.some_func', side_effect=TypeError)  # return_value='something'

def test_with(mocker):

    some_func() == 'yello'

    # 2 sposob mockowania
    mocker.patch('test_basics.some_func', side_effect=TypeError)  # return_value='good bye'

    with pytest.raises(TypeError):
        some_func()

    mocker.patch('test_basics.some_func', return_value='xxx')
    assert some_func() == 'xxx'



def test_dupa(dupa):
    assert dupa == 999


def test_env_variable_three():
    env_variable = os.getenv('AAA_VARIABLE')  # this test will see autouse fuxture defined in test_autouse.py ??
    assert env_variable == 'aaa_variable_name_dude'



db = []  # import db

def test_adding_to_db():
    db.append(9)
    assert len(db) == 1
    assert db[0] == 9

def test_is_previously_test_save_operation_on_db():
    assert len(db) == 1
    assert db[0] == 9

# actually this is bad behaviour (but not wrong)
# from that reason i should use something like setUp in every like that db tested function :)