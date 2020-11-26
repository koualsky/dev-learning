# Procedura REKURENCYJNE-WYSZUKIWANIE-BINARNE(A, p, r, x)
# 1. Jeśli p > r to zwróć NIE-ZNALEZIONO
# 2. W przeciwnym razie (p < r) wykonaj, co następuje:
#   A. Nadaj q wartość flor (p + r) / 2
#   B. Jeśli A[q] = x to zwróć q
#   C. W przeciwnym razie (A[q] not= x), jeśli A[q] > x, to zwróć
#       REREKURENCYJNE WYSZUKIWANIE BINARNE (A, p, q-1, x)
#   D. W przeciwnym razie (A[q] < x) zwróć
#       REKURENCYJNE-WYSZUKIWANIE-BINARNE(A, q+1, r, x)

lista = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'f', 'f', 'f', 'g', 'h', 'i', 'j']


def rekurencyjne_wyszukiwanie_binarne(A, p, r, x):
    if p > r:
        return 'NIE-ZNALEZIONO'
    else:
        # A
        q = int((p + r) / 2)

        # B
        if A[q] == x:
            return q
        else:
            # C
            if A[q] > x:
                return rekurencyjne_wyszukiwanie_binarne(A, p, q - 1, x)
            # D
            else:
                return rekurencyjne_wyszukiwanie_binarne(A, q + 1, r, x)


# wywołanie funkcji
print(rekurencyjne_wyszukiwanie_binarne(lista, 0, len(lista), 'g'))

# -----------------------------------------------------------------------------

# Procedura WYSZUKIWANIE-BINARNE(A, n, x)
# 1. Ustaw p na 1 i r na n
# 2. Dopóki p <= r, wykonuj, co następuje:
#   A. Nadaj q wartość floor (p+r)/2
#   B. Jeśli A[q] = x, to zwróć q
#   C. W przeciwnym razie (A[q] not= x), jeśli A[q] > x, to ustaw r na q - 1
#   D. W przeciwnym razie (A[q] < x), ustaw p na q + 1
# Zwróć nie znaleziono


def wyszukiwanie_binarne(A, n, x):
    p = 0
    r = n
    kroki = 0
    while p <= r:
        kroki += 1
        q = int((p + r) / 2)
        if A[q] == x:
            return str(q) + ' kroki: ' + str(kroki)
        else:
            if A[q] > x:
                r = q - 1
            else:
                p = q + 1
    return 'NIE-ZNALEZIONO'


# wywołanie funkcji
print(wyszukiwanie_binarne(lista, len(lista) - 1, 'i'))  # 12 powinno zwrocic przy i


# Procedura SORTOWANIE-PRZEZ-WYBIERANIE(A, n)
# Dane wejściowe:
# - A: tablica
# - n: liczba elementów w A do posortowania.
# Wynik: elementy tablicy A są posortowane w porządku niemalejącym (czyli rosnącym, bez sensu to nazwali...)
# 1. Dla i=1 do n-1:
#   A. Przypisz zmiennej najmniejszy indeks najmniejszego elementu w podtablicy A[i...n]
#   B. Zamień A[i] z A[najmniejszy]
#
# Procedura na nowo SORTOWANIE-PRZEZ-WYBIERANIE(A, n)
# Dane wejściowe: jak wyżej
# 1. Dla i = 1 do n - 1:
#   A. Przypisz zmiennej najmniejszy wartość i
#   B. Dla j = i + 1 do n:
#       i. Jeśli A[j] < A[najmniejszy], to podstaw j do najmniejszy
#   C. Zamień A[i] z A[najmniejszy]
#
# Procedura SORTOWANIE-PRZEZ-WYBIERANIE(A, n) - po mojemu
# 1. Porównaj element drugi z pierwszym i jeżeli mniejszy od pierwszego to zamień
# 2. Porównaj trzeci z pierwszym
# 3. ...
# ... teraz na pierwszym miejscu mamy na pewno najmniejszy element, więc pomijamy już pierwsze miejsce
# 4. Porównaj trzeci z drugim
# 5. i tak do n-1

# Sortowanie przez wybieranie
def swap(L, i, k):
    temp = L[i]
    L[i] = L[k]
    L[k] = temp
    return L


def select_sort(L):
    left = 0
    right = len(L) - 1
    for i in range(left, right):
        k = i
        for j in range(i + 1, right + 1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)
    return L

# Procedura SORTOWANIE-PRZEZ-WSTAWIANIE(A, n)
# 1. Dla i = 2 do n:
#   A. Ustaw klucz na A[i] i podstaw do j wartość i-1
#   B. Dopóki j>0 i A[j] > klucz, wykonuj, co następuje:
#       i. Podstaw A[j] do A[j + 1]
#       ii. Zmniejsz j o 1 (tzn. podstaw do j wartość j-1)
#   C. Podstaw klucz do A[j+1]

# Sortowanie przez wstawianie


def insertion_sort(A):
    for i in range(1, len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    return A


# Procedura SORTOWANIE-PRZEZ-SCALANIE(A, p, r) - NIE WYSZŁA MI JAK COŚ TO POWTÓRZYĆ
# ! UWAGA ! - procedura ta do działania potrzebuje skutecznej metody scalaj()
#
# Dane wejściowe:
#   A: tablica
#   p, r: początkowy i końcowy indeks podtablicy A
# Wynik: elementy podtablicy A[p..r] posortowane w porządku niemalejącym.
# 1. Jeśli p>=r, to podtablica A[p..r] ma najwyżej 1 element, jest więc już
#    posortowana. Powróć zatem, nie wykonując niczego.wykonując
# 2. W przeciwnym razie wykonaj, co następuje:
#    A. Nadaj q wartość int((p+r)/2)
#    B. Wywołaj rekurencyjnie SORTOWANIE-PRZEZ-SCALANIE(A, p, q)
#    C. Wywołaj rekurencyjnie SORTOWANIE-PRZEZ-SCALANIE(A, q+1, r)
#    D. Wywołaj SCALANIE(A, p, q, r)
#
# Procedura SCALAJ(A, p, q, r)
# Dane wejściowe:
#   A: tablica
#   p, q, r: indeksy do tablicy A. W przypadku każdej z podtablic: A[p..q] i
#   A[q+1, r], zakłada się, że jest już posortowana
# Wynik: podtablica A[p..r] zawiera elementy występujące pierwotnie w A[p..q] i
# A[q+1, r], obecnie jednak cała podtablica A[p..q] jest posortowana.
# 1. Nadaj n1 wartość q-p+1, a n2 wartość r-q
# 2. Niech B[1..n1+1] i C[1..n2+1] będą nowymi tablicami
# 3. Skopiuj A[p..q] do B[1..n1] oraz A[q+1..r] do C[1..n2]
# 4. Ustaw zarówno B[n1+1], jak i C[n2+1] na infinity
# 5. Ustaw i oraz j na 1
# 6. Dla k = p do r:
#   A. Jeśli B[i] <= C[j], to przypisz B[i] do A[k] i zwiększ i o 1
#   B. W przeciwnym razie (B[i] > C[j]) przypisz C[i] do A[k] i zwiększ j o 1

# próba zaimplementowania metody scalaj wg instrukcji z książki
def scalaj_z_ksiazki(A):
    p = 0
    r = len(A) - 1
    q = int((p + r + 1) / 2)
    #n1 = q - p + 1
    #n2 = r - q
    B = A[p:q]
    C = A[q + 1:r]
    i = 1
    j = 1
    for k in range(r + 1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[i]
            j += 1
    return A

# moja implementacja funkcji scalaj po przeanalizowaniu tego własnym mózgiem
# na wejściu przyjmuje 2 tablice, obie posortowane rosnąco
# na wyjściu wypuszcza jedną scaloną posortowaną rosnąco


def scalaj(A, B):
    C = []
    for e in A + B:
        if not B:
            C.append(A[0])
            A.remove(A[0])
        elif not A:
            C.append(B[0])
            B.remove(B[0])
        elif A[0] <= B[0]:
            C.append(A[0])
            A.remove(A[0])
        elif A[0] >= B[0]:
            C.append(B[0])
            B.remove(B[0])
    return C


"""
Procedura NAPRAWDE_PROSTE_SORTOWANIE(A, n)
Dane wejściowe:
- A: tabklica, której elementami są tylko 1 lub 2
- n: liczba elementów w A do posortowania
Wynik: elementy A są posortowane w porządku niemalejącym.
1. Nadaj k wartość 0
2. Dla i = 1 do n:
    A. Jeśli A[i] = 1, to zwiększ k o 1.
3. Dla i = 1 do k:
    A. Podstaw 1 do A[i]
4. Dla i = k + 1 do n:
    A. Podstaw 2 do A[i]
"""


def naprawde_proste_sortowanie(A):
    # DANE WEJŚCIOWE
    A = A
    n = len(A)

    # OBLICZENIA
    k = 0
    for i in range(n):
        if A[i] == 1:
            k += 1

    for i in range(k):
        A[i] = 1

    for i in range(k, n):
        A[i] = 2

    # WYNIK
    return A


"""
Procedura OBLICZ-TABELE-LCS(X, Y)

Dane wejściowe: X i Y - dwa napisy długości, odpowiednio m i n
Wynik: tablica l[0..m, 0..n]. Wartość l[m, n] jest długością najdłuższego 
wspólnego podciągu X i Y
1. Niech l[0..m, 0..n] będzie nową tablicą
2. Dla i = 0 do m:
    A. Nadaj l[i, 0] wartość 0
3. Dla j = 0 do n:
    A. Nadaj l[0, j] wartość 0
4. Dla i = 1 do m:
    A. Dla j = 1 do n
        i. Jeśli xi jest takie samo jak yi, to nadaj l[i, j] wartość l[i-1, j-1] + 1
        ii. W przeciwnym razie (xi różni się od yi) nadaj l[i, j] wartość większą
        z l[i, j-1] i l[i-1, j]. Jeśli l[i, j-1] równa się l[i-1, j], to nie ma 
        znaczenia, którą wybierzesz
5. Zwróć tablicę l
"""


def oblicz_tabele_lcs(X, Y):
    # Dodatkowe dane wejściowe
    m = len(X)
    n = len(Y)

    # 1, 2, 3
    l = []

    for e in range(m + 1):
        l += [[0 for i in range(n + 1)]]

    # 4
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                if l[i][j - 1] > l[i - 1][j]:
                    l[i][j] = l[i][j - 1]
                else:
                    l[i][j] = l[i - 1][j]

    # WYNIK
    return l


"""
Procedura ZESTAWIAJ-LCS(X, Y, l, i, j)

Dane wejściowe:
    X i Y: dwa napisy
    l: tablica wypełniona przez procedurę oblicz-tabelę-lcs
    i oraz j: indeksy do, odpowiednio, X i Y, a także do l
Wynik: LCS (najdłuższy wspólny podciąg) Xi i Yi
1. Jeśli l[i, j] równa się 0, zwróć napis pusty
2. W przeciwnym razie (ponieważ l[i, j] jest dodatnie, więc również i oraz j są
dodatnie), jeżeli xi jest taki sam jak yj, zwróć napis utworzony najpierw przez 
rekurencyjne wywołanie  ZESTAWIAJ-LCS(X, Y, l, i-1, j-1), a następnie dodanie 
na jego końcu xi (lub yj)
3. W przeciwnym razie (xi różni się od yj), jeśli l[i, j-1] jest większe niż 
l[i-1, j], zwróć napis przekazany przez rekurencyjne wywołanie 
ZESTAWIAJ-LCS(X, Y, l, i, j-1)
4. W przeciwnym razie (xi różni się od yj i l[i, j-1] jest mniejsze lub równe 
l[i-1, j], zwróć napis przekazany przez rekurencyjne wywołanie 
ZESTAWIAJ-LCS(X, Y, l, i-1, j))
"""


def zestawiaj_lcs(X, Y, l, i, j):

    # 1, 2
    if l[i + 1][j + 1] == 0:
        return ''
    else:
        if X[i] == Y[j]:
            return zestawiaj_lcs(X, Y, l, i - 1, j - 1) + X[i]  # ????????????
        else:
            if l[i][j - 1] > l[i - 1][j]:
                return zestawiaj_lcs(X, Y, l, i, j - 1)
            else:
                return zestawiaj_lcs(X, Y, l, i - 1, j)


def szyfruj_cezarze(text):
    """
    1. Przypisz do zmiennej text - tekst do zamiany
    2. n = długość tekstu
    3. Stworz tablice wszystkich znakow
    4. m = długość wszystkich znaków
    5. Dla każdego znaku w text:
        a. określ indeks tego znaku w text
        b. określ indeks tego znaku w all_chars
        c. zmień ten znak z text na +3
    """

    # input
    n = len(text)
    all_chars = 'abcdefghijklmnouprstwvqxyz abcd '
    exit_text = ''

    # calculations
    for e in text:
        i = all_chars.index(e)
        exit_text += all_chars[i + 3]

    # output
    return exit_text


def odszyfruj_cezarze(text):
    """
    odwrócona kalkulacja metody szyfrującej
    """

    # input
    n = len(text)
    all_chars = 'abcdefghijklmnouprstwvqxyz abcd '
    exit_text = ''

    # calculations
    for e in text:
        i = all_chars.index(e)
        exit_text += all_chars[i - 3]

    # output
    return exit_text


def kompresuj(text):
    """
    Input: 
        - text: tekst do skompresowania
    Output: 
        - text_tab: tablica z unikatowymi słowami użytymi w tekście
        - text_code: tablica z tekstem uporządkowanym wg indeksów
    Calculations:
        1. Przyjmij tekst wejściowy
        2. Zrób puste tablice: text_tab i text_code
        3. Zrób tablice raw_text z tekstu text - każde słowo osobno
        4. Dla każdego elementu z tablicy raw_text:
            a. Jeżeli słowo jest już w text_tab:
                - Dodaj do text_code jego index z text_tab
            b. Jeżeli tekstu nie ma w text_tab:
                - Dodaj element do text_tab
                - Dodaj do text_code jego index z text_tab
        5. Stwórz tablicę dwuwymiarową code i dodaj do niej text_tab i text_code
        6. Zwróć tablicę
    """

    # Input
    text = text
    text_tab = []
    text_code = []
    raw_text = text.split(' ')

    # Calculations
    for word in raw_text:

        # If word is in text_tab
        if word in text_tab:
            text_code.append(text_tab.index(word))

        # If don't
        else:
            text_tab.append(word)
            text_code.append(text_tab.index(word))

    # Output
    code = [text_tab, text_code]
    return code


def dekompresuj(code):
    """
    Input:
        - tablica dwuwymiarowa z:
          1. słowami - text_tab
          2. kolejnością słów - text_code

    Calculations:
        1. Stwórz z tablicy dwuwymiarowej 2 tablice jednowymiarowe:
            - text_tab
            - code_tab
        2. Stwórzy pusty string
        3. Dla każdego kodu z code_tab:
            a. dodaj do stringa text z tablicy text_tab o indeksie 
               danego kodu
            b. dodaj do stringa spację
        4. Zwróć stringa

    Output:
        - tekst ułożony z słów z tablicy text_tab wg kolejności z text_code
    """

    # Input
    text_tab = code[0]
    code_tab = code[1]
    string = ''

    # Calculations
    for code in code_tab:
        string += text_tab[code]
        string += ' '

    # Output
    return string


# select_sort
lista = [12, 9, 3, 7, 14, 11]
print(select_sort(lista))

# insertion_sort
lista = [12, 9, 3, 7, 14, 11]
print(insertion_sort(lista))

# scalanie (moje)
listaA = [2, 3, 9, 11, 12, 13, 19, 43, 129, 300]
listaB = [1, 3, 7, 8, 10, 20, 56]
print(scalaj(listaA, listaB))

# really_simple_sort
A = [1, 2, 1, 1, 1, 2]
print(naprawde_proste_sortowanie(A))

# najdłuższy ciąg wspólnych znaków
X = 'CATCGA'
Y = 'GTACCGTCA'

# wynik i wydruk wyniku
#  x  y
#  m  n
#  i, j
#l[0][9] = 9
# print(A[2][9])
l = oblicz_tabele_lcs(X, Y)
for e in l:
    print(e)

i = len(X) - 1
j = len(Y) - 1

# print zestawiaj_lcs
print(zestawiaj_lcs(X, Y, l, i, j))

text = 'hej jestem maciej zeta a ty'
print('text przed: ' + text)

text = szyfruj_cezarze(text)
print('zaszyfrowany: ' + text)

text = odszyfruj_cezarze(text)
print('odszyfrowany: ' + text)

# testy kompresji
text = '''
A black hole is a region of spacetime exhibiting gravitational acceleration 
so strong that nothing no particles or even electromagnetic radiation such as 
light can escape from it. The theory of general relativity predicts that a 
sufficiently compact mass can deform spacetime to form a black hole.
The boundary of the region from which no escape is possible is called the 
event horizon. Although the event horizon has an enormous effect on the fate 
and circumstances of an object crossing it, no locally detectable features 
appear to be observed. In many ways, a black hole acts like an ideal black 
body, as it reflects no light. Moreover, quantum field theory in 
curved spacetime predicts that event horizons emit Hawking radiation, with 
the same spectrum as a black body of a temperature inversely proportional to 
its mass. This temperature is on the order of billionths of a kelvin for 
black holes of stellar mass, making it essentially impossible to observe.

Objects whose gravitational fields are too strong for light to escape were 
first considered in the 18th century by John Michell and Pierre-Simon 
Laplace. The first modern solution of general relativity that would 
characterize a black hole was found by Karl Schwarzschild in 1916, although 
its interpretation as a region of space from which nothing can escape was 
first published by David Finkelstein in 1958. Black holes were long 
considered a mathematical curiosity; it was during the 1960s that theoretical 
work showed they were a generic prediction of general relativity. The 
discovery of neutron stars by Jocelyn Bell Burnell in 1967 sparked interest 
in gravitationally collapsed compact objects as a possible astrophysical 
reality.
'''
print('PRZED KOMPRESJA: ' + text)
compressed = kompresuj(text)
print('   PO KOMPRESJI: ' + str(compressed))
decompressed = dekompresuj(compressed)
print(' PO DEKOMPRESJI: ' + str(decompressed))

print('                               oryginalny text: ' + str(len(text)))
print('skompresowany text + kod skompresowanego textu: ' + str(len(compressed[0]) + len(compressed[1])))
