from unittest import TestCase


def add_integer(*args: int) -> int:
    """Gets integers and sum them.

    Note:
        Do not use minus numbers.

    Args:
        *args: Two or more integers.

    Returns:
        Result of summing all integers given as arguments.
    """

    if len(args) <= 1:
        raise ValueError(f'You should provide at least 2 arguments. But you provide {len(args)}')
    if not all(isinstance(e, int) for e in args):
        raise TypeError('All given arguments should be integers')
    if not all(e >= 0 for e in args):
        raise ValueError('Given arguments should be greater than 0.')
    return sum(args)


class TestMathObject(TestCase):
    def test_add_integer_no_arguments(self):
        with self.assertRaises(ValueError):
            add_integer()

    def test_add_integer_one_argument(self):
        with self.assertRaises(ValueError):
            add_integer(1)

    def test_add_integer_two_arguments(self):
        assert add_integer(0, 0) == 0
        assert add_integer(0, 1) == 1
        assert add_integer(1, 2) == 3

    def test_add_integer_wrong_argument_type(self):
        with self.assertRaises(TypeError):
            add_integer('a', 'b')
            add_integer({}, {})

    def test_add_integer_minus_values(self):
        with self.assertRaises(ValueError):
            add_integer(-1, 9)
