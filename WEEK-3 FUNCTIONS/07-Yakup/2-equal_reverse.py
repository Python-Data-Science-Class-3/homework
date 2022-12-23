# Write a function that controls the given inputs whether they are equal to their reversed order or not.
# Example:

# Input >>> madam, tacocat, utrecht
# Output >>> True, True, False

results=[]
a = True

def equal_reverse(my_str):
    new_str = reversed(my_str)
    result =(new_str!=my_str )
    return(result)

while  a:
    value = list(input("Enter your massage : "))     # madam, tacocat,utrecht

    if len(value)>=1 : 
        results.append((equal_reverse(value)))
       
    elif (len(value)) < 1 :                          # If you press 'enter' without typing a message, the program will close.
         a=False   
print(results)  