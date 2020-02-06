with open('some_file', 'a') as f:
    f.write('Hola!')


'''
The above code is equvalent to this code:

file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
'''


# w - write
# a - append
# r - read
