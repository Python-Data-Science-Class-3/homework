#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:
#Function call: unique_list([1,2,3,3,3,3,4,5,5])
#Output : [1, 2, 3, 4, 5]
#written by Nuseybe at 19.12.2022


list= [1,2,3,3,3,3,3,4,5,5,6]
def uniq(list):
    print(set(map(lambda set: set, list)))  #sorting lıst for order
uniq(list)