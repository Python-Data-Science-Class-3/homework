#Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. 
#Ignore case, ignore blanks and assume the user does not enter any punctuation. 
#Display a two-column table of the letters and their counts with the letters in sorted order.
# Example Input This is a sample text with several words 
#This is more sample text with some different words Output 
# [('a', 4), ('d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

'''
1) PEP 8 --> https://peps.python.org/pep-0008/#comments

2) Alfabetik siraya gore hangi harften kac adet kullanildigini bizden istemisti,
burdaki cozumde ise cumledeki harflerin sirasina gore kac adet oldugunu bulmusuz, 
buyuk kucuk harfleri de farkli olarak hesapliyor, mesela buyuk A ile kucuk a farkliymis gibi.

Butun alfabeyi bir string halinde olusturup, bu string uzerinde donerek degerlendirme yapip,
olmayan harfleri hic donguye dahil etmeyip, 
olanlarla da alfabetik siraya gore kac adet olduguyla birlikte bir sozluk olusturup,
bu sozlugun liste olarak cagirilmasini deneyin.

Yukardaki haritaya gore once kendiniz deneyin, daha sonra ise asagidaki ornek cozumu incelersiniz.
'''

sentence = input("enter a sentence")

letter = dict()
for x in sentence: 
    if x in letter: 
        letter[x] += 1
    else:
        letter[x] = 1
for x, y in letter.items():
    print([x, ":", y])


'''
letter_list = []
count_list = []
user_sentence_input = input('Sentence:')
user_sentence_input = user_sentence_input.lower(

letter_dictionary = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    count = user_sentence_input.count(i)
    if count == 0:
        continue
    letter_dictionary[i] = count
    
print(letter_dictionary.items())
'''