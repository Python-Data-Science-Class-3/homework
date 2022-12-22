#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:
#Function call: unique_list([1,2,3,3,3,3,4,5,5])
#Output : [1, 2, 3, 4, 5]

letters = ["a","a","b","c","c","d","f","e","e","g","h","h","j"] 

def unrepeated(letters):
    unrepeated_list = []
    s = set(letters)

    for letter in s:
        unrepeated_list.append(letter)
    return sorted(unrepeated_list) #added sort() for alphabetical order

print(unrepeated(letters))    