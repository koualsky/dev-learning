"""
----------------------------------
| MUTABLE | IMMUTABLE            |
|---------+------+---------------|
| list    | int, float (numbers) |
| dict    | string               |
| set     | tuple                |
----------------------------------
"""

# INT, FLOAT (numbers)
a = 1
b = a
a = 2
print(f'a={a}, b={b}')  # a=2, b=1

# STRING
a = 'antonio'
b = a
a = 'banderas'
print(f'a={a}, b={b}')  # a='banderas', b='antonio'

# TUPLE
a = (1, 2, 3)
b = a
print(f'a={a}, b={b}')  # a=(1, 2, 3), b=(1, 2, 3)



# LIST
a = ['a', 'b', 'c']
b = a
b[0] = 'z'
print(f'a={a}, b={b}')  # a=['z', 'b', 'c'], b=['z', 'b', 'c']

a = ['a', 'b', 'c']
b = a[:]  # OR list(a) OR x_list.copy() OR import copy and: copy.copy(a) - copy only this list with references inside OR copy.deepcopy(a) - copy this object and copy all nested objects inside
b[0] = 'z'
print(f'a={a}, b={b}')  # a=['a', 'b', 'c'], b=['z', 'b', 'c']

# DICT
a = {'a': 'aaa', 'b': 'bbb'}
b = a
b['a'] = 'zzz'
print(f'a={a}, b={b}')  # a={'a': 'zzz', 'b': 'bbb'}, b={'a': 'zzz', 'b': 'bbb'}

a = {'a': 'aaa', 'b': 'bbb'}
b = a.copy()
b['a'] = 'zzz'
print(f'a={a}, b={b}')  # a={'a': 'aaa', 'b': 'bbb'}, b={'a': 'zzz', 'b': 'bbb'}

# SET
a = {1, 2, 3}
b = a
b = {2, 3, 4}
print(a)
print(b)

# --------------------------------------

a = [1, 2, 3]
b = a
b[0] = 9
print(a == b)
print(a is b)

# --------------------------------------
import sys
print(sys.getrefcount(a))  # 3
print(sys.getrefcount(1))  # 216 - but this is references used in python itself.
