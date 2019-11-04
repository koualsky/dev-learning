squares = [e + 1 for e in range(10)]
print(squares)

dirtyfruits = ['   banana', '   loganberry  ', 'passion fruit     ']
cleanfruits = [e.strip() for e in dirtyfruits]
print(cleanfruits)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec = [num for e in vec for num in e]
print(vec)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

a = 'annamariajopek'
a = set(a) # wyodrebnia wszystkie litery bez powtorzen. litery z ktorych sklada sie zdanie
print(a)