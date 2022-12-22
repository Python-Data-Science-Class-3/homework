"""
Write a function that filters all the unique(unrepeated) elements of a given list.

Example:

Function call: unique_list([1,2,3,3,3,3,4,5,5])

Output : [1, 2, 3, 4, 5]
"""



def uniquelist(numbers_list):
    return sorted(list(set(numbers_list)))

print (uniquelist([1,2,6,8,4,9,13,2,2,2,5,5,5,4]))