'''
Developer   : Musab SARI
Date        : 13.12.2022

Application : Set of Two Words

Explanation : Set of two words is an application where user inputs two words and outputs in a list as follows shared letters of the words, unique letters of word one
and unique letters of word two.
'''

list_of_outputs = [] #list created to be able to see desired output
word_1 = set(input('Word 1:')) #user input for word1
word_2 = set(input('Word 2:')) #user input for word2

shared_letters  = (''.join(sorted(list(word_1&word_2)))) #functions of the application
diffirence1 = (''.join(sorted(list(word_1-word_2))))
diffirence2 = (''.join(sorted(list(word_2-word_1))))

list_of_outputs[0:3] = shared_letters, diffirence1, diffirence2 #output block

print(list_of_outputs) 