import unittest
from unittest.mock import patch
from datetime import datetime
from app import is_weekday


class TestApp(unittest.TestCase):

    # today = monday
    @patch('app.today', datetime(year=2020, month=5, day=4))
    def test_is_weekday_monday(self):
        self.assertTrue(is_weekday())

    # today = sunday
    @patch('app.today', datetime(year=2020, month=5, day=10))
    def test_is_weekday_sunday(self):
        self.assertFalse(is_weekday())


if __name__ == '__main__':
    unittest.main()
