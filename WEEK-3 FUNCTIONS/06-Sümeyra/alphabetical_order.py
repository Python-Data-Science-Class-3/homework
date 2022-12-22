#Write a function that takes an input of different words with hyphen (-) in between them and then:
#sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.
#Example:
#Input >>> green-red-yellow-black-white
#Output >>> black-green-red-white-yellow

words = input("Please enter different words with hyphen (-) in between them:")
words_list = words.split('-')
words_list.sort()

def alphabetical_order(words):
    return '-'.join(words)
print(alphabetical_order(words_list))