"""
Namedtuple is good idea for representing records or objects like point.
"""

from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])

adam = Rec('Adam', age=40, jobs=['dev', 'mgr'])

# We have access to this object via index or argument

print(adam)
print(adam[0])
print(adam.name)

# Or we can display this namedtuple as a dict

print(adam._asdict())
d = adam._asdict()
print(d['jobs'])

# And use this object as a dict
name, age, job = d.values()
print(job, name, age)

# And...

name, age, jobs = adam
print(name, age, jobs)

