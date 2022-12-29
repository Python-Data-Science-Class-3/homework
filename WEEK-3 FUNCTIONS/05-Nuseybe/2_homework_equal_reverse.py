#Write a function that controls the given inputs whether they are equal to their reversed order or not.
#Example:
#Input >>> madam, tacocat, utrecht
#Output >>> True, True, False
#written by Nuseybe at 19.12.2022
word = input ("Please write a word:  ")   #inputıng a word
word_rev= word[::-1]                   # word is reversing 
def reverse_word():                    #function for comparing two values
    #print(word_rev)
    print( word_rev == word)           #comparing
reverse_word()                        
