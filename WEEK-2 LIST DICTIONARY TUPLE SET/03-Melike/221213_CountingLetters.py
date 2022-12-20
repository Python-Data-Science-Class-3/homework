#Write a code snippet that inputs a sentence from the user, 
# then uses a dictionary to summarize the number of occurrences of each letter. 
# Ignore case, ignore blanks and assume the user does not enter any punctuation. 
# Display a two-column table of the letters and their counts with the letters in 
# sorted order. 

# Example Input This is a sample text with several words 
# This is more sample text with some different words 
# Output [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), 
# ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

'''
1) Yukardaki yorum satirlarini tirnak isareti icerisinde de yazabilirsiniz.

2) Yazim hayet anlasilir, okunakli. Yorum satirlarini hizalamak icin bu kadar ugrasmaya gerek yok,
koddan sonra 2 bosluk, sonrasinda # isareti, ondan sonra da 1 bosluk ve sonrasinda yorum.

3) Kodda alfabetik siraya gore hangi harfin kac adet oldugunu istiyor bizden,
siz cumledeki gelis sirasina gore harfleri dizmissiniz.
Bir alfabe stringi olusturup bunun uzerinde dongu ile donuyoruz.
Hangi harften kac adet oldugunu bir sozluk icinde olusturup,
dict.items() komutu ile ciktimizi aliyoruz.

4) Once biraz deneyip uzerinde dusunun, daha sonra asagidaki cozumu incelersiniz.
'''

input1 = (str(input("You may write something here: "))).lower()     # to ignore upper cases
dict = {}                                                           # to create an empty dictionary

for i in input1:
    m = {i: input1.count(i)}                                        # to count the each letter in the string and,  
    dict.update(m)                                                  # to add those letter numbers into the empty dictionary

a = dict.pop(" ")                                                   # to pop out the blanks
# print(dict)

k = list(i for i in dict.items())                                   # to create a list of the items in the dictionary
print(k)

'''
#Calculation of letter numbers of the entered sentence
a = str( input("Enter the sentence")).lower()
print (a)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#Search each letter within the alphabet 
sozluk = {}
for i in alphabet: 
#For not print letters that are not in the entered sentence and take the value "0"
    if a.count(i) > 0:
        sozluk[i] =  a.count(i)
        
print(sozluk.items())
'''