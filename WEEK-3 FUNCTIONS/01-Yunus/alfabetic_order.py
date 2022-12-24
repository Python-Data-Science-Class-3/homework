## 3-alphabetical_order.py

# Write Splitted function that takes an input of different words with hyphen (-) in between them and then:
# sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.

# Example:
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow 

#-----------------Made by Yunus Donmez--------------21/12/2022
def alfabetich_order():

    '''
    This function sort input words and write it back.
    '''
    mylist = input("write some words with a '-' in between:\n")
    Splitted=mylist.split('-')   #Splits given words with an '-' 
    Ordered=sorted(Splitted)         
       
    print('-'.join(Ordered))

alfabetich_order()
