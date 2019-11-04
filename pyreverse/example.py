"""
Pyreverse create UML diagram from classes!
Go to this directory and type: pyreverse -o png example.py
"""


class Wheel:
    """Wheel"""

    def __init__(self, size):
        self.__size = size
        self.public = None

    def run(self):
        return True


class CarComp:
    """Car - Composition"""

    def __init__(self, wheel_size):
        self.wheel1 = Wheel(wheel_size)
        self.wheel2 = Wheel(wheel_size)
        self.wheel3 = Wheel(wheel_size)
        self.wheel4 = Wheel(wheel_size)


class CarAggr:
    """Car - Aggregation"""

    def __init__(self, wheel_obj1, wheel_obj2, wheel_obj3, wheel_obj4):
        self.wheel1 = wheel_obj1
        self.wheel2 = wheel_obj2
        self.wheel3 = wheel_obj3
        self.wheel4 = wheel_obj4
