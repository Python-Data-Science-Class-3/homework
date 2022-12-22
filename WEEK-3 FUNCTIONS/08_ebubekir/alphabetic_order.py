"""3-alphabetical_order.py
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.
Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
"""
a=input("write a word:")
b=input("write a word:")
c=input("write a word:")
print(a,b,c,sep="-")                          #seperate the inputs with -
given=[a,b,c]                                 #define a list by inputs
given.sort(reverse=False)                     #sorted the strings
list_to_string='-'.join(map(str,given))       #join the strigs and seperate the sorted strings  with -
print(list_to_string)                         #call and print the function 