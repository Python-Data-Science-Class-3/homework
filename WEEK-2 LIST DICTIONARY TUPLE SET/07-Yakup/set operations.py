'''

Write a program that takes in two words as input and returns a list containing three elements, 
in the following order Shared letters between two words. Letters unique to word 1. Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations.
The strings will always be in lowercase and will not contain any punctuation.

Example
Input1 :sharp 
Input2  :soap 
Output ['aps', 'hr', 'o']
 
 '''
s1 = set("sharp")
s2 = set("soap")
x=[]

x1=list(s1.union(s2).difference(s1.symmetric_difference(s2)))    #take the combination and then We got the difference of the union.
x2=list(s1.difference(s2))                                       #we got the difference
x3=list(s2.difference(s1))                                       #we got the difference


x3.sort(),x1.sort(),x2.sort()                                    #We did alphabetical order.
x=[x1,x2,x3]
print(x)




