"""
What can I add to this example? This works like a generator.
"""

my_list = [1, 2, 3]
print(*my_list)

"""
List to variables
"""

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a)
print(b)
print(c)

"""
Merging list.
"""

list_first = [1, 2, 3]
list_second = [4, 5, 6]
merged_list = [*list_first, *list_second]
print(merged_list)
merged_list_2 = [*list_first, list_second]
print(merged_list_2)

"""
Dicts.
"""

first_dict = {"A": 1, "B": 2}
second_dict = {"C": 3, "D": 4}
merged_dict = {**first_dict, **second_dict}
print(merged_dict)

"""
String to list.
"""

a = [*"Macius"]
print(a)

"""
OR
"""

*a, = "Maciusiek"
print(a)