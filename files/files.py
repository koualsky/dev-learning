"""
Files only store strings.
We can store lists and dicts as a string, and read and back them to the program via eval() function
Also, we can store objects with the pickle module!

Files are buffered by default. Which means, they are transferred to the disk only if we close() the file or after call
flush() method. Why? Because searching in file loaded to the memory is a way more faster than reading file from disk
each time where we try to find something inside file.
Buffering means that file is in memory. We can search, index on them.
Until we call close or flush method. Then file is transferred to the disk.

Close method ends the connection with external file, and releases tied to it system resources.
Saves buffer to the disk and clean buffer.
Calling close() method is a good practice. Unless we are using the context manager then we don't have to.

We can turn off buffering, by setting third argument (0) in open method, but this inefficient and this is bad idea.

--------------------------------------------------------------------------------------
output = open('data', 'w')      # Creates file for saving (data / data.txt / data.bin)
                                # Path for default is where the script exists.
                                # But we can put there absolute path for particular system, e.g. (adios/docs/data.txt)
input = open('data', 'r')       # Opens file for reading. We do not have to give them 'r' argument. 'r' is default
a_string = input.read()         # Loads all file to one string (with \n signs)
a_string = input.readline()     # Loads only first line. Each next call readline() loads next line of file. (with \n)
a_string = input.readlines()    # Loads all file to the list of strings (with \n signs)
output.write(a_string)          # Write string (or bytes) to the file. Python by default wont save endfile sing (\n)
output.writelines(a_list)       # Write all strings from list to the file (line by line). We need to add '\n' sign
                                # on each string if we have to save each string line by line.
output.close()                  # Transfer buffer to the file and close connection with file.
output.flush()                  # Transfer buffer to the file without closing connection to the file.
any_file.seek(n)                # Change position in file to the offset 'n' for the next operation
                                # So if we set offset to 0 <- this is begginning of the file. If we set 1, we will
                                # overwrites everything after first sign on this file.
                                # n - means just index, like in the string. But index is on the whole scope of file.
                                # So the lines do not count.
for line in open('data'):       # Iterative reading file - line by line
    print(line)
"""


# Example of saving list and dict to the file, and read them again with eval() function

file = open('eval_file', 'w')
l = ['hello', 'world']
d = {'name': 'John', 'age': 50}
file.write(f'{str(l)}${str(d)}\n')
file.close()

file = open('eval_file')
line = file.readline()
parts = line.split('$')
l = eval(parts[0])
d = eval(parts[1])
print(type(l))      # list
print(l)
print(type(d))      # dict
print(d)


# Example of saving object to the file, and read them with pickle module

class Custom:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print(f'{self.name} have {self.age} years!')


# Try
adam = Custom('Adam', 44)
adam.say_my_name()

# Let's pickle!
file = open('pickle_file.pkl', 'wb')
import pickle
pickle.dump(adam, file)
file.close()

# Read the pickle!
file = open('pickle_file.pkl', 'rb')
adam = pickle.load(file)
print(adam)
adam.say_my_name()

# So I can save objects with pickle module, but if I want to read my own custom objects,
# I need to import my custom class and then load pickled object.

# But if I use dict or list for pickle, I dont need nothing else. It just work :)
