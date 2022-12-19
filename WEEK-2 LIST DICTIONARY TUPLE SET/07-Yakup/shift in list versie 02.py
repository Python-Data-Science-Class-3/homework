"""
Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left)
when n is positive (negative).
Use wrap-around if an element is shifted beyond the end of the list,
then continue to shift starting at the beginning of the list. 

EXAMPLE
Inputs [1, 2, 3, 4, 5],   2 
Output [4, 5, 1, 2, 3] 
Inputs [1, 2, 3, 4, 5],  -2 
Output [3, 4, 5, 1, 2]
"""

print("\n")
l = list(input("Enter list elements without space: "))
n = int(input("Enter shift amount: "))
l = [int(x) for x in l]                                 #Reconstructing list elements that are strings as integers

print("\nfirst list :",l)

if n < 0:
    "delete the first element from the list and after deleting it," \
    " print the frozen value '(l.pop(0)) ' at the end of the list."
    while n < 0:
        l.insert(len(l), l.pop(0))                     #Delete the first element of the list and write it to the last index.
        n += 1
else:
    while n > 0:
        l.insert(0, l.pop())                           # Delete the last element of the list and write it to the first index.
        n -=1

print("\n last list  :",l)


