#Write a code snippet that inputs a sentence from the user, 
# then uses a dictionary to summarize the number of occurrences of each letter. 
# Ignore case, ignore blanks and assume the user does not enter any punctuation. 
# Display a two-column table of the letters and their counts with the letters in 
# sorted order. 

# Example Input This is a sample text with several words 
# This is more sample text with some different words 
# Output [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), 
# ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

input1 = (str(input("You may write something here: "))).lower()     # to ignore upper cases
dict = {}                                                           # to create an empty dictionary

for i in input1:
    m = {i: input1.count(i)}                                        # to count the each letter in the string and,  
    dict.update(m)                                                  # to add those letter numbers into the empty dictionary

a = dict.pop(" ")                                                   # to pop out the blanks
# print(dict)

k = list(i for i in dict.items())                                   # to create a list of the items in the dictionary
print(k)

