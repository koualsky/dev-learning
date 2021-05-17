"""
If U want to implement comparisons to your object, U need to implement this functions:
__eq__  -  ==
__ne__  -  !=
__lt__  -  <
__le__  -  <=
__gt__  -  >
__ge__  -  >=

Before we implement this functions, we should decide which value will we compare.
It could be age, it could be name length. Anything.
Here it will be age.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other

    def __ne__(self, other):
        return self.age != other

    def __lt__(self, other):
        return self.age < other

    def __le__(self, other):
        return self.age <= other

    def __gt__(self, other):
        return self.age > other

    def __ge__(self, other):
        return self.age >= other


adam = Person('Janek', 19)
maciek = Person('Maciek', 34)
eustachy = Person('Vincent', 41)

print(adam > maciek)    # False
print(adam >= maciek)   # False
print(adam < maciek)    # True
print(adam <= maciek)   # True
print(adam == maciek)   # False
print(adam != maciek)   # True
