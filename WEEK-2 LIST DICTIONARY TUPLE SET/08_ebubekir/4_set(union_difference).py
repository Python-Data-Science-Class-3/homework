"""
Write a program that takes in two words as input and returns a list containing three elements,
in the following order Shared letters between two words.
Letters unique to word 1. Letters unique to word 2. Each element of the output should have unique letters,
and should be alphabetically sorted. Use set operations. 
The strings will always be in lowercase and will not contain any punctuation.
Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']
"""
a=input("write a word:")
b=input("write a second word:")
a=a.lower()      #lower characters
b=b.lower()
a1=set(a)        #converted a,b to set
a2=set(b)
c1=''.join(sorted(a1&a2))    
c2=''.join(sorted(a1-a2))    
c3=''.join(sorted(a2-a1))
"""etters unique to word 1. Letters unique to word 2. Each element of the output should have unique letters,
and should be alphabetically sorted. Use set operations. """
liste=[c1,c2,c3]
print(liste)
