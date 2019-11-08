"""
DEBUGGING LESSON

How to debug with pdb:
	$ python -m pdb buggy.py

Or interactively:
	>>> import pdb
	>>> import buggy
	>>> buggy.crash()
	>>> pdb.pm()

Usually start debugging here (in debugging py file):
	import pdb
	pdb.set_trace()

	# usually in main:
		import pdb; pdb.set_trace()

Usually pdb commands:
	l(ist)
	n(ext)
	c(ontinue)
	s(tep)
	r(eturn)
	b(reak)
	And python
"""

print('1')
print('2')
print('3')
print('4')
print('5')
print('6')
print('7')
print('8')