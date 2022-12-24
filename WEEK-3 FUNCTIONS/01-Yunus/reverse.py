# 2-equal_reverse.py
# Write a function that controls the given inputs whether they are equal to their reversed order or not.

# Example:
# Input  >>> madam, tacocat, utrecht 
# Output >>> True, True, False

#-----------------Made by Yunus Donmez--------------21/12/2022
def reverse():
    '''
    This function write a given word in reversed way

    '''
    given_words=input("Enter one or multiple words with a comma and a space : \n")
    given_words=given_words.split(', ')         # Splits words and designates in list given_words 
    result =[]
    for i in given_words:                       # Loop for every items in given_words
        reversed_versie=i[::-1]                 # Place every element reversed in list reversed_versie
        if i==reversed_versie:                  # Is reversed version same with the word itself??
            result.append("True")
        else:
            result.append("False")
    print(", ".join(result))
            
reverse()
