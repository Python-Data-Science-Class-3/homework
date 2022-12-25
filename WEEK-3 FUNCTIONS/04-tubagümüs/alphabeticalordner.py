'''Developer : Tuba GÜMÜS ESMEK
   Date      : 20.12.2022
   Sukject   :Alphabetical Order


'''
#alphabetical_order.py
#Write a function that takes an input of different words with hyphen (-) in between them and then:
#sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.
#example:
#Input >>> green-red-yellow-black-white
#Output >>> black-green-red-white-yellow

def regulator():     #creating a function
    mywords = input("write your words with '-' :\n")  #creating a word group
    mywords = sorted(mywords.split('-')) 
    # sorting the listalphabetically with the sorted command
    #split between words with (-) 
    return print(mywords)

regulator()