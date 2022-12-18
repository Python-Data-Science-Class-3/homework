"""
Write a program that takes two inputs;
one of them is a list and the other is a number,
and returns the list obtained by shifting the elements
in the list n places to the right (left) when n is positive (negative).
Use wrap-around if an element is shifted beyond the end of the list,
then continue to shift starting at the beginning of the list.
Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]
"""
s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]         #define a list
n=int(input("what is the number of steps:"))    #input lenght of the list
f=[]
for i in range(1,len(s)+1):
    if i+n<=len(s):
        f.append(s[i+n-1])
    else:
        f.append(s[i-len(s)+n-1])
print(f)

