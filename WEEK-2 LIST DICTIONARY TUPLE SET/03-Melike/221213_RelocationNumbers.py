#Write a program that takes two inputs; one of them is a list and the other is a number, 
# and returns the list obtained by shifting the elements in the list n places to the right (left) 
# when n is positive (negative). Use wrap-around if an element is shifted beyond the end of the list, 
# then continue to shift starting at the beginning of the list. 
# Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] 
# Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]

list1 = list(input("Please input a list of items without space between them: "))
n = int(input("Please input a number: "))
u = len(list1)
newlist = ['x' for i in range(u)]                       # to make a default list in the length of list1

print("\n")

for i in range(u):
    newindex = (i + n) % u                              # to reduct the new index with modulus if it is more than the length of our list 
    newlist[newindex] = list1[i]                        # to assign elements to new indexes
print(newlist)