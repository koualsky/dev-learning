# rekurencyjnie z stringa
def rek_print(n):
    if n != 0:
        print(n)
        rek_print(n - 1)

rek_print(6)