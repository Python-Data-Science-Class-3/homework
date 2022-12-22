"""Unique elements function
Function is written for filtering and ordering the repeated 
elements in the list entered by the user.
"""


def uniq_element(x):
#Entering list items from the user
    x = (set(input("lütfen liste elemanlarını giriniz"))) 
    return(x)
#sorting and printing filtered elements
print(sorted(uniq_element(x)))
