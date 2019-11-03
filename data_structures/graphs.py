# W pythonie grafy możemy wygodnie przedstawić za pomocą słowników i list.
# Graf będzie słownikiem, w którym kluczami będą wierzchołki (liczby, napisy, itp.)
# Każdemu kluczowi będzie odpowiadać lista zawierająca wierzchołki połączone
# krawędzią z danym wierzchołkiem

# PRZYKŁAD. Rozważmy graf skierowany o wierzchołkach od A do F i krawędziach
# (A,B), (A,C), (B,C), (B,D), (C,D), (D,C), (E,C). Możemy go zapisać jako słownik

# http://users.uj.edu.pl/~ufkapano/algorytmy/lekcja14/python1.html
# https://www.python.org/doc/essays/graphs/

"""
A -> B
A -> C
B -> C
B -> D
C -> D
D -> C
E -> C
F -> C
"""

graph = {
    "A":["B","C"],
    "B":["C","D"],
    "C":["D"],
    "D":["C"],
    "E":["C"],
    "F":["C"]
}