# BIN (binarny):      0, 1
# OCT (osemkowy):     0, 1, 2, 3, 4, 5, 6, 7
# INT (dziesietny):   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# HEX (szesnastkowy): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f

numb_int = 10
numb_bin = bin(numb_int)  # 1010
numb_oct = oct(numb_int)  # 12
numb_hex = hex(numb_int)  # a

print(f'BIN: {numb_bin[2:]}')
print(f'OCT: {numb_oct[2:]}')
print(f'INT: {numb_int}')
print(f'HEX: {numb_hex[2:]}')

from_bin_to_int = int(numb_bin, 2)
from_oct_to_int = int(numb_oct, 8)
from_hex_to_int = int(numb_hex, 16)
print(from_bin_to_int)
print(from_oct_to_int)
print(from_hex_to_int)
