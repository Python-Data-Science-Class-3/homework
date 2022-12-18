'''
DEVELOPER : TUBA GÜMÜS ESMEK
DATE      : 15.12.2022
SUBJECT   :SHARED LETTERS
'''

#Write a program that takes in two words as input and 
# returns a list containing three elements, in the following order Shared letters between two words. 
# Letters unique to word 1. Letters unique to word 
# 2. Each element of the output should have unique letters, and should be alphabetically sorted. 
# Use set operations. The strings will always be in lowercase and will not contain any punctuation. 
# Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']



w1 = set(input("write first word:\n"))
w2 = set(input("write second word:\n"))
lst1 = list(sorted(w1.intersection(w2))) # intersection of two words
#print(''.join(lst1))                    # sorting the lst1

lst2 = list(sorted(w1.difference(w2))) # difference of the w1 form w2
#print(''.join(lst2))                  # sorting the lst2         

lst3 = list(sorted(w2.difference(w1))) #difference of the w2 from w1
#print(''.join(lst3))                  # sorting the lst3

new_list = [''.join(lst1),''.join(lst2),''.join(lst3)] 
print(new_list)
