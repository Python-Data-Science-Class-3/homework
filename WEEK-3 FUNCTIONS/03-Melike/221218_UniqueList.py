"""
1-unique_list.py
Write a function that filters all the unique(unrepeated) elements of a given list.

Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output       : [1, 2, 3, 4, 5]"""

def unique_list(list1):
    set1 = set(list1)           # to convert the given list into set to remove repetation
    list2 = list(set1)          # to convert the set into list again for the result
    return list2

print(unique_list([1,2,3,3,3,3,4,5,5]))