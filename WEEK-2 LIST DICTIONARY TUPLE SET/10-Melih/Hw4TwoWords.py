""" 

Developer : Melih Orhan Yilmaz
Date      : 15.12.2022

Application : Shifting

Explanation : Write a program that takes in two words as input and returns a list containing three elements, in 
the following order Shared letters between two words. Letters unique to word 1. Letters unique to word 2. Each 
element of the output should have unique letters, and should be alphabetically sorted. Use set operations. The 
strings will always be in lowercase and will not contain any punctuation. Example Input1 sharp Input2 soap Output 
['aps', 'hr', 'o']

 """

a = input("Write a word: ".lower())
b = input("Write a word: ".lower())
set1 = set(list(a)) # List to set
set2 = set(list(b)) # List to set
print(set1)
print(set2)
a = set1 - set2 
b = set2 - set1
c = set1 & set2

lst = ''.join(a) , ''.join(b) , ''.join(c) # Combining set elements
print(list(lst))