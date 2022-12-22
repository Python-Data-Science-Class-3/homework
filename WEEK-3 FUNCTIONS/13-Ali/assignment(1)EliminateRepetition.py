# # Python_Week3  (EliminateRepetition)

# ## 1-unique_list.py
# Write a function that filters all the unique(unrepeated) elements of a given list.

# Example:

# Function call: unique_list([1,2,3,3,3,3,4,5,5])

# Output       : [1, 2, 3, 4, 5]
while True:
    gathering = input('enter please your wish arguments to liset\
        without any other characters: ')
    def elemination(deviation):
        a = list(set(deviation))
        print(a)
    elemination(gathering)
