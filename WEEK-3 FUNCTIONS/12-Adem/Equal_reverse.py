""" This function that controls the given inputs whether 
they are equal to their reversed order or not.
"""
# User enters list elements
string = (list(input("Enter the elements leaving a space between them.").split()))
# Writing the list for check the result
print(string)
def reverse(string):
# loop to control each element
    for i in string:
        if i == i[::-1]:
            print("True")
        else:
            print("False")
reverse(string)

"""
Gayet guzel, basarili. 

"""

'''
def palindrome(string):  # define a function, palindrome()
    return string == string[::-1]  # we evaluate in reverse order whether the modified string is equal to the modified string
print(palindrome(string))  # if the string is palindrome, this returns TRUE, if it s not this return FALSE
'''