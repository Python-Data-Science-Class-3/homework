# Write a program that takes in two words as input and returns a list containing three elements, in the following order 
# Shared letters between two words. Letters unique to word 1. Letters unique to word 2. 
# Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. 
# The strings will always be in lowercase and will not contain any punctuation. 
# Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']

word1 = (input("Please input the first word: ")).lower()  # lower is to ignore upper cases
word2 = (input("Please input the second word: ")).lower()

w1 = set(list(word1))                                     # to generate a set with the letters of the strings
w2 = set(list(word2))

a1 = ''.join(str(i) for i in list(w1 & w2))               # "&" is for the shared letters and "-" is for the unique letters.
a2 = ''.join(str(i) for i in list(w1 - w2))               # "join" is to convert list (which is converted from set) to the string
a3 = ''.join(str(i) for i in list(w2 - w1))

print([a1, a2, a3])                                       # to return the result into a list
