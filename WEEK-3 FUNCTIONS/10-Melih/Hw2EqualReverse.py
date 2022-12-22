""" 

Developer : Melih Orhan Yilmaz
Date      : 21.12.2022

Application : Equal Reverse

Explanation : 
    Write a function that controls the given inputs whether they are equal to their reversed order or not.
    Example:
    Input >>> madam, tacocat, utrecht
    Output >>> True, True, False

"""

words = ["madam","tacocat","utrecht"]

def equal_reverse():

    list1 = [] # Create a list for True-False
    for i in words:
        if i == i[::-1]: # If words==reserveWords
            list1.append(True)
        else:
            list1.append(False)
        
    return list1

print(equal_reverse())