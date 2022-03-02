"""
conftest.py musi byc w nadrzednym / glownym folderze w ktorym sa testy i musi miec taka nazwe
czyli obok folderow w ktorych sa porozdzielane testy
sluzy do przechowywania fixtur
kazda stworzona tu fixtura, dostepna bedzie dla mnie w wszystkich testach
"""

import pytest


@pytest.fixture
def dupa():
    return 999


@pytest.fixture(autouse=True)  # autouse in fixure is like setUp in unittest
def dev_env(monkeypatch):      # monkeypatch is keywork here! with it we can patch config or env variables.
    monkeypatch.setenv("AAA_VARIABLE", "aaa_variable_name_dude")
    
