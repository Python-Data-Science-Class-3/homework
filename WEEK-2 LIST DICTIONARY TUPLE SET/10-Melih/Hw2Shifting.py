""" 

Developer : Melih Orhan Yilmaz
Date      : 14.12.2022

Application : Shifting

Explanation : Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is 
positive (negative). Use wrap-around if an element is shifted beyond the end of the list, then continue to 
shift starting at the beginning of the list. Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] 
Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]

 """

input1 = input("Create a list separated by space: ")
list = input1.split() # To separate list elements 
print(list)

n = int(input("Enter a number: ")) # How many times will the list shift
x = n % len(list) # The remainder when the number of shifts is divided by the number of the list
print(x)

# If the remainder is 0 when the number of shifts is divided by the number of the list
if x == 0:
    print(list)

# If the remainder is greater than 0 when the number of shifts is divided by the number of the list
elif x>0:
    newListRight = list[-x:] + list[:-x]
    print(newListRight)

# If the remainder is less than 0 when the number of shifts is divided by the number of the list
else:
    newListLeft = list[x:] + list[:x]
    print(newListLeft)
