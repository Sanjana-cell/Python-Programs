"""
Write a Python program to get a list, sorted in increasing order by the last element in
each tuple from a given list of non-empty tuples
"""

# take the second element for sort
def secondElement(element):
    return element[1]


# list
list_1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# sort list with key
sorted_list = sorted(list_1, key=secondElement)

# print list
print('Sorted list:', sorted_list)