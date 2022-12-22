"""
Write a function that controls the given inputs 
whether they are equal to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False"""

args=["madam","level","father","pop","tacocat","utrect"]     #define list 
palindrome=list(map(lambda string: string == string[::-1],args))    #if the string =revrsed(string), take it in the list
print(palindrome)
      