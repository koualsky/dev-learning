# ITERATORS
a = ('apple', 'banana', 'cherry')
it = iter(a)
print(next(it))
print(next(it))
print(next(it))


# GENERATORS just loop and make yield istead print (or return)
# but! doesn't zajmuje memory! robi all w locie. to sa obiekty 'generator'
# taka funkcja mozemy sobie stworzyc obiekt 'generator', ktory jest tak
# jakby lista po ktorej mozemy iterowac, ale nie zajmuje miejsca w memory!
# aha. i mogę iterować po tym za pomocą next. -> next(generator_obj)

def generatorex():
    num = 0
    while num < 100:
        num += 1
        yield num


'''
a = generatorex()
for e in a:
    print(e)'''
# OR

for e in generatorex():
    print(e)

'''
print('---')
g = generatorex()
print(next(g))
print(next(g))
print(next(g))'''