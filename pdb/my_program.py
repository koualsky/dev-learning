"""Set breakpoint:
import pdb; pdb.set_trace()
OR alternatively breakpoint() in python 3.7+ - works in exacs same way. import pdb and set set_trace()

Run pdb (in command line):
python3 -m pdb my_program.py

n - next
c - continue until next set_trace()
p c - po dojsciu do breakpointu komenda ta pokaze wartosc zmiennej c. jak bym wpisal p filename to pokaze wartosc filename
q - wychodzi
"""

def runsomething():
    a = 5
    b = 3
    c = a * b
    import pdb; pdb.set_trace()
    d = c + a
    e = d + b
    f = e + 1
    return f

def somethingelse():
    filename = __file__
    import pdb; pdb.set_trace()
    print(f'path = {filename}')

runsomething()
somethingelse()