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
    
    for word_list in word_list:    #returning  the parameter with a for loop
        if word_list == word_list[::-1]: #if the parameter is equal in rerverse order
         return True #True command
 #if the parameter is not equal in reverse, False command
    return False
    

words1 =["racecar","level", "reviver","redder"] #inverse equal words
words2 =["cheap","expensive", "home"]  #inverse unequal words


print(equal_reverse(words1))  #printing words
print(equal_reverse(words2))
