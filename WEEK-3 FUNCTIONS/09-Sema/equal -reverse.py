"""
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:

Input >>> madam, tacocat, utrecht

Output >>> True, True, False
"""





word=input("please enter a word:")
def equalreverse(words):
    newlist=[word for word in words if word==word[::-1]]
    return True
print(equalreverse(word))


#2. option
#def equal_reverse(words):

 #   if word==word.reverse():
  #      return True
   # else:
    #    return False
#word = list(input("Please Enter a Word:"))
#print (equal_reverse(word))
