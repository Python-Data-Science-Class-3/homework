""" 

Developer : Melih Orhan Yilmaz
Date      : 22.12.2022

Application : Alphabetical Order

Explanation : Write a function that takes an input of different words with hyphen (-) in between them and then:

sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.

    Example:

    Input >>> green-red-yellow-black-white

    Output >>> black-green-red-white-yellow

 """


def alphabetical_order():
    words=[i for i in input("Write a few words separated by space: ").split(' ')] # It is used to make lists of words and to split list elements.
    words.sort() # Sort in alphabetical order
    newwords = "-".join(words) # Adding "-" between words
    return newwords

print(alphabetical_order())