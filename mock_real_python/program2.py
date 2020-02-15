"""
Mock służy do udawania obiektów. Nie robi kompletnie nic. Aby działał jak udawane obiekty,
trzeba po prostu wstrzyknąć do mockowanego obiektu - properties and methods z realnego obiektu.

A do mockowanego obiektu łatwo przypisujemy rzeczy, np
obiekt = Mock()
obiekt.jakis.costam = realna.funkcja(day=7)

i pozniej mozemy to wywolac tak: obiekt.jakis.costam()

----------

How to configure mock?
1.
mock = Mock()
mock.configure_mock(return_value=True)
mock() # return True

2.
mock = Mock()
mock.return_value = 5
mock() # return 5
"""

import requests
import unittest
from unittest.mock import Mock

# Mockujemy request po to by kontrolować go
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return j.json()
    return None


# Testujemu
class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()