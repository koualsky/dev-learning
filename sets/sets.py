# SETS - ZBIORY

a = {1, 2, 8}
b = {2, 3, 4}

result_or = a | b   # {1, 2, 3, 4, 8} - every unique values from both sets (if element is in one of this sets -> add to result)
result_xor = a ^ b  # {1, 3, 4, 8} - reversed version of OR (if element is in both of this sets -> NOT add to result)
result_and = a & b  # {2} - only common elements
result_exclude = b - a  # {3, 4}  removes from set b only these values which are in set a

print(result_or)
print(result_xor)
print(result_and)
print(result_exclude)

# ---------------------------------------------------

a = {'adam', 'tomasz', 'jacek'}

print('maciej' in a)   # False
print('adam' in a)     # True
print({'tomasz'} < a)  # True (tomasz zawiera się w zbiorze a)

# ---------------------------------------------------

engineers = {'robert', 'amadeusz', 'anna', 'aleksander'}
managers = {'edward', 'amadeusz'}

# 'robert' in engineers  # True
# engineers & managers   # ('amadeusz') - is engineer and manager
# engineers | managers   # {'edward', 'amadeusz', 'anna', 'robert', 'aleksander'} - all from both categories
# engineers - managers   # {'robert', 'aleksander', 'anna'} Engineers who are not Managers
# managers - engineers   # {'edward'} Managers who are not Engineers
# engineers > managers   # False. All managers are engineers?
# {'robert', 'amadeusz'} < engineers  # True. They are engineers?