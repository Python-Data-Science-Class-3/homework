# Write a function that takes an input of different words with hyphen (-) in between them and then:
# sorts the words in alphabetical order, 
# adds hyphen icon (-) between them,
#  gives the output of the sorted words.

# Example:
# Input >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow


def wordSorted(my_string:str):
    terms = my_string.split()           #We split the string expression as a list before sorting it.
    terms.sort(key=str.lower)           #To sort the string expression alphabetically.
    output = "-".join(terms)
    return (output)

statement = input("Enter your massage : ")
print(wordSorted(statement))