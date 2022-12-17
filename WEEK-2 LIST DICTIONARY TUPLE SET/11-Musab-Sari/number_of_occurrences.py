'''
Developer   : Musab SARI
Date        : 13.12.2022

Application : Number of Occurrences

Explanation : The application is created with an intention to be able to see occurrences of the letters in a sentence.  
'''

letter_list = []
count_list = []
user_sentence_input = input('Sentence:')
user_sentence_input = user_sentence_input.lower() #to ignore case
for i in 'abcdefghijklmnopqrstuvwxyz': #to check every letter in the alphabet in sequence and append them to the lists and to ignore space and punctuation
    count = user_sentence_input.count(i)
    letter_list.append(i)
    count_list.append(count)

letter_dictionary = {letter_list[j]: count_list[j] for j in range(26) if count_list[j] >= 1} #creating dictionary and 'if block' is there for elimination of 0 count values. 
#26 is the number of letters in the alphabet

list_letter_dictionary = [] #created this block to see desired output, otherwise the values in the dictionary were printed out in {}. 
for item in letter_dictionary.items():
    list_letter_dictionary.append(item)
print(list_letter_dictionary)