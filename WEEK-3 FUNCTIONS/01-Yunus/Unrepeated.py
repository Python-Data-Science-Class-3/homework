## 1-unique_list.py

# Write a function that filters all the unique(unrepeated) elements of a given list.

# Example:
# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]


#-----------------Made by Yunus Donmez--------------21/12/2022
def unrepeated(TheList):
    '''
    a function that filters all the unique(unrepeated) elements of a given list
    '''

    new_set = set(TheList)     # Turns into a set which automaticaly removes repaeted values
    print(sorted(new_set))
TheList = input("Enter a something to see its uniq values: ")
unrepeated(TheList)

