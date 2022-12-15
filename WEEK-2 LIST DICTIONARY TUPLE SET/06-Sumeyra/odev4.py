#Write a program that takes in two words as input and returns a list containing three elements, in the following order Shared letters between two words. 
#Letters unique to word 1. Letters unique to word 2. 
# Each element of the output should have unique letters, and should be alphabetically sorted. 
#Use set operations. 
#The strings will always be in lowercase and will not contain any punctuation.
#Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']


input1=set(input("Enter a word1: "))
input2=set(input("Enter a word2: "))
a=list(set(input1)&set(input2)) #use set operation
b=list(set(input1)-set(input2))
c=list(set(input2)-set(input1))
print(sorted(a)) #to sort an inputs
print(sorted(b))
print(sorted(c))
print("".join(a),"".join(b),"".join(c)) #combines the list of sorted

