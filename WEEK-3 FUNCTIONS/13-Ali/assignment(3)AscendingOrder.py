
# ## 3-alphabetical_order.py  (AscendingOrder)
# Write a function that takes an input of different 
# words with hyphen (-) in 
# between them and then:

# sorts the words in alphabetical order, adds
# hyphen icon (-) between them,
# gives the output of the sorted words.
# Example:
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow 
while True:
    words = input("please enter words to be sorted\
with \"-\" between them: ").split('-')  
    seperated = sorted(words)
    wordsWithHyphen = '-'.join(seperated)
    print("\n \n \n sorted words: "\
,wordsWithHyphen,2*"\n ")

    

