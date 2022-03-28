class Bag:
    def __init__(self, *moneys):
        self.moneys = moneys
    
    def __str__(self):
        for money in self.moneys:
            print(money)


class Money:
    def __init__(self, value: int):
        self.value = value
    
    def __str__(self):
        return f'Money {self.value}'


# money_15 = Money(15)
# money_11 = Money(11)
# money_3 = Money(3)
# money_1 = Money(1)
# bag = Bag(money_15, money_11, money_3, money_1)

moneys = [Money(130), Money(99), Money(87), Money(17), Money(9), Money(3), Money(1)]
bag = Bag(*moneys)

print(bag)
