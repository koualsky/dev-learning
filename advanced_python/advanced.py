# 1
from collections import defaultdict
items = ["one", "two", "three"]
backpack = defaultdict(int)
for item in items:
    backpack[item] += 1
print(backpack)

# 2
from collections import namedtuple
Point = namedtuple("Point", "x y")  # namedtuple creates simple class. x y -> arguments for init. tuple is immutable, so i can't do e.g. p1.x = 7
p1 = Point(20, 30)
p2 = Point(-5, 20)
print(p1, p2)
print(p1.x)
# p1.x = 3  # this returns error

# 3
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
i = iter(days)
print(i)
print(next(i))
print(i)
print(i)
for day, i in enumerate(days, 7):
    print(day, i)

# 4
polish_days = ["Nied", "Pon", "Wt"]
zipped = zip(days, polish_days)
for day in zipped:
    # print(day)  # will return tuple with first object from first list and first object from second list. and so on.
    print(f"{day[0]}: {day[1]}")

# 5
import itertools
cycle = itertools.cycle(days)  # Instead returning exception after ending this list, cycle will looped our given list
for _ in range(10):
    print(next(cycle))

# 6
count = itertools.count(3, 8)
print(next(count))
print(next(count))
print(next(count))

# 7
def isEven(num):
    if num % 2 == 0:
        return True
    return False
nums = (1, 8, 12, 54, 199, 24566, 9, 35)
evens = list(filter(isEven, nums))  # with filter function I can remove all ";", some words and so on...
print(evens)

# 8
def square(num):
    return num**2
squares = list(map(square, nums))
print(squares)

# 9
# But "wyrażeniami listowymi" we can make the same things as filter() and map()

# 10
grades = (5, 30, 68, 50, 100, 87, 76)
grades = sorted(grades)
print(grades)

def grade(num):
    if num < 10:
        return "Failed"
    if num >= 10 and num <= 60:
        return "Passed"
    if num > 60:
        return "Superpower!"

real_grades = list(map(grade, grades))
print(real_grades)

# 11
distances = [50, 24, 100, 120, 50]
distance_in_km = [e * 1.6 for e in distances]
print(distance_in_km)

# or

def calculate(num):
    return num * 1.6
distance_in_km = [calculate(e) for e in distances]
print(distance_in_km)

# 12 wyrazenie slownikowe
distance_dict = {x: y for x, y in zip(distances, distance_in_km)}
print(distance_dict)

# 13
def something(x: str = "nothing", y: int = 2):
    return x * y
print(something("hello", 5))
print(something())

# 14
class RGBClass:
    def __init__(self):
        self.red = 10
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return self.red, self.green, self.blue
        raise AttributeError

    def __dir__(self):
        return ["rgbcolor"]

RGB = RGBClass()
print(RGB.rgbcolor)
# print(RGB.some)  # returns Attribute color
print(dir(RGB))




# ---------------------

from enum import Enum
Animal = Enum('Animal', 'ant bee cat dog')
print(Animal.cat)
print(Animal.cat.name)
print(Animal.cat.value)

Colors = Enum('Colors', 'red green blue')
print(Colors.red.value)
print(Colors.green.value)
print(Colors.blue.value)

def abc(num):
    return num + num

listka = [1, 2, 3, 4, 5]
ress = map(abc, listka)
for e in ress:
    print(e)

def xoxo(num):
    if num != 4:
        return num

yyy = filter(xoxo, listka)
for e in yyy:
    print(e)

def funct(*args, **kwargs):
    for e in args:
        print(e)

    # hmm to jest iterowane w args... to juz sie nie wykonuje
    for key, value in kwargs.items():
        print(key, value)

funct(10, 20, 30, 40, {"a": 100, "b": 200, "c": 300})

# ------

numb = [1, 4, 2, 99, 32]
print(sorted(numb))