'''Developer : Tuba GÜMÜS ESMEK
   Date      : 20.12.2022
   Subjekt   : Unique Lis
'''

#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:
#unction call: unique_list([1,2,3,3,3,3,4,5,5])
#Output : [1, 2, 3, 4, 5]


numbers = [1,2,3,3,3,4,5,5,] #repeat element list
def unique_list(numbers):   #creating a function
    unique_list1 = []        #define a new list
    for x in numbers:        # creating elements of new list with for loop
        if x in unique_list1: 
            continue
        elif x not in unique_list1:
             unique_list1.append(x)
    return unique_list1
        
print(unique_list(numbers))  