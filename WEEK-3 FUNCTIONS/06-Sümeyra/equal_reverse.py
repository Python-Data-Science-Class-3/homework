#Write a function that controls the given inputs whether they are equal to their reversed order or not.
#Example:
#Input >>> madam, tacocat, utrecht
#Output >>> True, True, False

string = input("word:") 

def palindrome(string):    #define a function,palindrome()
  return string == string[::-1] #we evaluate in reverse order whether the modified string is equal to the modified string
print(palindrome(string))  #if the string is palindrome,this returns TRUE,if it s not this return FALSE