numbers=[1,2,3,3,3,3,4,5,5]    #define a list
def uniq_nums(numbers):        #define a function
    list=[]                    #create an empty list 
    for i in numbers:
        if i not in list:      #take every character once
            list.append(i)     #add chosen character to the list
    return list
print(uniq_nums(numbers))      #call the function 