""" 

Developer : Melih Orhan Yilmaz
Date      : 20.12.2022

Application : Unique List

Explanation : 
    Write a function that filters all the unique(unrepeated) elements of a given list.
    Example:
    Function call: unique_list([1,2,3,3,3,3,4,5,5])
    Output : [1, 2, 3, 4, 5]

"""

lst = [1,2,3,3,3,3,4,5,5]

def unique_numbers():
  
    results = list(map(int, sorted(set(lst))))  # set(lst): Converting list to set, so that same elements are not repeated
                                                # sorted: to sort the list
                                                # list(map(....)): Converting list to set and to make the string an int

    return results

print(unique_numbers())