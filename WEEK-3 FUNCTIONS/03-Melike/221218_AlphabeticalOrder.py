"""
3-alphabetical_order.py
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.

Example:
Input  >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow """

def alphabetical_order(words):
    words = words.split("-")
    words2 = sorted(words)
    words3 ="-".join(words2)
    print (words3)

alphabetical_order("green-red-yellow-black-white")

"""
Gayet guzel. 
Bunu kullanicidan input alarak gelen girdileri kullanarak tekrar duzenleyelim.
"""