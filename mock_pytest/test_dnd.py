# How to test? In this directory type: pytest test.py
# If I have name started by 'test' and then '_dnd' (module name), I can type just: pytest

from dnd import attack_damage
from unittest import mock


@mock.patch("dnd.randint", return_value=5, autospec=True)
def test_attack_damage(mock_randint):
    assert attack_damage(1) == 6
    mock_randint.assert_called_once_with(1, 8)

"""
Nie kumam do końca. Obejrzeć wykłady z tego i porobić coś.
"""