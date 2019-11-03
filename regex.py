import re

text = 'hej my name is lolek@wp.pl an i am the lolo@op.pl an you dude@oo.com?'

wynik = re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z]*', text)

print(wynik)