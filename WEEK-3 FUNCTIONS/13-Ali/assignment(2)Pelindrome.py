# ## 2-equal_reverse.py
# Write a function that controls the given inputs whether they are 
# equal to their reversed order or not.
# Example:
# Input  >>> madam, tacocat, utrecht 
# Output >>> True, True, False

# def pelindrome(entry):
    
#     if entry[0] != entry[-1]:
#         return False
#     else:
#         discard() # burası yarım kaldı
#         return pelindrome(entry)
# pelindrome(input("enter word to check whether it's pelindrome: "))


while True:
    def pelindrome(entry):
        try:
            if entry[0] != entry[-1]: #in this step first and last letter are checked whether are the same
                return False
            else:
                entry.pop(0)  # if code comes here first and last letters are the same
                entry.pop(-1) # they are moved here so that next lettes to check
                return pelindrome(entry)
        except IndexError: # in line "if" you have an Error since our list ist emtpty it signs all letters met the symmetrically equal condition and were deleted 
            return True    # therefore its pelindrome 
            
   
    print(pelindrome(list(input("enter a word to check whether it's \
pelindrome: ").lower())))
    
    
    
    
    
            
    
    
    
    
    