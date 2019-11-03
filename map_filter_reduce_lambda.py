# MAP()
def something(e):
    return e + e

a = map(something, ['a', 'b', 'c'])
for e in a:
    print(e)




# FILTER()
def lyxx(e):
    if e != 4:
        return e

b = filter(lyxx, [1, 2, 3, 4, 5])
for e in b:
    print(e)




# REDUCE() and LAMBDA
from functools import reduce
c = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)  # ((((1+2)+3)+4)+5)
print(c)
