""" 

Developer : Melih Orhan Yilmaz
Date      : 14.12.2022

Application : Letters

Explanation : Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the 
number of occurrences of each letter. Ignore case, ignore blanks and assume the user does not enter any punctuation.
Display a two-column table of the letters and their counts with the letters in sorted order. Example Input This is 
a sample text with several words This is more sample text with some different words Output [('a', 4), ('d', 3),
('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), 
('t', 9), ('v', 1), ('w', 4), ('x', 2)]

 """

sentence = input("Write a text: ")
sentence1 = sentence.replace(" ","") # Ignore the space
print(sentence1)

counts = dict() # Dictionary for letters
letters = [] # List for letters
for letter in sentence1: 
    letters.append(letter) # Creating a list with the letters of the sentence with the for loop
    if letter in counts:
        counts[letter] += 1 # Adding +1 in the same letters in the if case
    else:
        counts[letter] = 1 # It stays the same number in same letters in the else case
            
for i in sorted(counts.items()): # Sort dictionary by key and print one after the other with a for loop
    print(i)