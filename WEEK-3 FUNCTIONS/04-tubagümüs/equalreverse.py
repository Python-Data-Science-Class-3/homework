'''
Developer : Tuba GÜMÜS ESMEK
Date      : 19.12.2022
Subject   : Equal Reverse
'''
#equal_reverse
#Write a function that controls the given inputs whether they are equal to their reversed order or not.

#Example:

#Input >>> madam, tacocat, utrecht

#Output >>> True, True, False

#kelime = list(reversed(kelime))

def equal_reverse(word_list):  #creatin the function
    
    word_list =list(reversed(word_list))  #sort parameter in reverse order to create a List
    
    for i in word_list:    #returning  the parameter with a for loop
        if i == i[::-1]: #if the parameter is equal in rerverse order
         return True #True command

    else:
         return False
 #if the parameter is not equal in reverse, False command
         
    

#palindrom words =["racecar","level", "reviver", "redder"] #inverse equal words
#other words =["cheap","expensive", "home"]  #inverse unequal words

words = (list(input("write a palindrom word:\n ").split('-')))
print(equal_reverse(words))