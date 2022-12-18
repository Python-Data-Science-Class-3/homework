'''Write a code snippet that inputs a sentence from the user, then uses a dictionary
to summarize the number of occurrences of each letter. Ignore case, ignore blanks
and assume the user does not enter any punctuation. Display a two-column table of 
the letters and their counts with the letters in sorted order. Example Input This
is a sample text with several words This is more sample text with some different
words Output [('a', 4), ('d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3),
('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1),
('w', 4), ('x', 2)]'''

initialStr = input("Enter some text to analyze letters in it: ")
# import string
# print(string.printable) # in this step the alphabet letters are taken 
#from terminal setting from the resul of printable: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterNumber = {x:initialStr.count(x) for x in initialStr if x in alphabet}
print([(k,v) for k,v in letterNumber.items()])




