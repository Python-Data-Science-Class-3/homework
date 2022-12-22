#Write a function that takes an input of different words with hyphen (-) in between them and then:
# sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.
# Example:Input >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow
#written by Nuseybe at 21.12.2022

word=input("enter the 5 words  using '-'  between:  ")   #inputing words
print(word)
def sort_word():                                    #function for split, sort and join to words
    l=word.split('-') 
    l.sort() 
    print('-'.join(l))
sort_word()