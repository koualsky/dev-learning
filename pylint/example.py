"""
Go to this directory and type: pylint example.py
"""


class Human:
    """This is doc string"""

    def __init__(self, name):

        self.__name = name

    def hey(self):
        """Hey"""

        return self.__name + ' ho'

    def honest(self):
        """Ho"""

        return self.__name + ' oho'
