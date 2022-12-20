'''
This program calculates Shared letters between two words. Letters unique to word 1. 
Letters unique to word 2. 

'''

A = set(input("Firts woord: "))
B = set(input("Second woord : "))

C = [(A&B),(A-B),(B-A)]
print(sorted(C))