#Write a function that filters all the unique(unrepeated) elements of a given list.
#Example:

#Function call: unique_list([1,2,3,3,3,3,4,5,5])

#Output : [1, 2, 3, 4, 5]

new_list= []
my_list=[1,2,2,22,222,3,3,20,20,20,40,40,5,5]


def unique_list(value):
    new_list.append(value)
    return ((new_list))

    
for i in my_list:
    if i not in new_list:
        new_list= unique_list(i)
new_list.sort()        
print(new_list)