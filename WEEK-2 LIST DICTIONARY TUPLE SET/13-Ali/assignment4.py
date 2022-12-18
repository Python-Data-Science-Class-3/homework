'''Write a program that takes in two words as input and returns
a list containing three elements, in the following order Shared 
letters between two words. Letters unique to word 1. Letters unique
to word 2. Each element of the output should have unique letters,
and should be alphabetically sorted. Use set operations. The strings 
will always be in lowercase and will not contain any punctuation. 
Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']'''
word1 = input("Enter first word:")
word2 = input("Enter second word:")
list1 = list(word1)
list2 = list(word2)
common = []
for e in list1:
    if e in list2:
       common.append(e) 
common2 = []
for e in list1:
    if e not in list2:
       common2.append(e) 
common3 = []
for e in list2:
    if e not in list1:
       common3.append(e) 
a = ' '.join(common)
b = ' '.join(common2)
c = ' '.join(common3)
eventualList = [a, b,c ]
print(eventualList)