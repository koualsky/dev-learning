# with - creates for us 'local' temporary context.
# We can operate in this context and after exit from this context, they close everything.

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

# -----------------------------------------

import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))  # >>> Decimal(0.33)

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))      # >>> Decimal(0.333333333...)
