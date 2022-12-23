'''Developer : Tuba GÜMÜS ESMEK
   Date      : 20.12.2022
   Subjekt   : Unique Lis
'''

#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:
#unction call: unique_list([1,2,3,3,3,3,4,5,5])
#Output : [1, 2, 3, 4, 5]


repeated_list = [1,2,3,3,4,5,6,6,7,8,8,] #repeat element list

def unique_list (numbers):   #creating a function
    unique_list1 = []        #define a new list
    for x in numbers:        # creating elements of new list with for loop
        if numbers in unique_list1:  
            continue
        else:
            unique_list1.append(numbers)
        
        
    print(unique_list(numbers)) 