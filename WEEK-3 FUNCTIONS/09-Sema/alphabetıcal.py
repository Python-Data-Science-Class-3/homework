""""
Alphabetic Order
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. 
Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
"""

def alphabetical(word):
  b = word.split('-')
  b.sort()
  c = '-'.join(b)
  return c

a = input('Entera few different words with hyphen: ')
print(alphabetical(a))
