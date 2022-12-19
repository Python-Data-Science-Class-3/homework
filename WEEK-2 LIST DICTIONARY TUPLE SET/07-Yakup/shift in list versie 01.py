
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

new_list = (list(input("please share a new list:")))
n = (int(input("write a number:")))
print(F" n is = {n}  My list is = {new_list}")


if n >0 :               #If our value is a positive value, then this part will work.

    new_list1 = new_list[n:] + new_list[:n]
    print("My new list =", new_list1)


elif n<0 :             #I made a new form here, this code will work for the negative side.

    new_list1 = new_list[(-n):(n)] +new_list[n:] + new_list[:-n]      # our scrolled list....

print("My new list =", new_list1)