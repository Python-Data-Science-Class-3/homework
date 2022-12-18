'''
Developer   : Musab SARI
Date        : 13.12.2022

Application : Number of Occurrences

Explanation : The application is created with an intention to be able to see occurrences of the letters in a sentence.  
'''

letter_list = []
count_list = []
user_sentence_input = input('Sentence:')
user_sentence_input = user_sentence_input.lower()  # to ignore case
for i in 'abcdefghijklmnopqrstuvwxyz':  # to check every letter in the alphabet in sequence and append them to the lists and to ignore space and punctuation
    count = user_sentence_input.count(i)
    # Buraya 'if' satiri ile 'continue' ekleyebilirsin, 
    # bu sayede bir sonraki satira gecmeden donguye bir sonraki elemandan devam eder,
    # boylece asagidaki gibi bir dongu kurmana da gerek kalmaz, 
    # islem ve variable kalabaligi azalir ve kod daha hizli calisir.
    # su anda olmasa da karmasik ve bilgisayari zorlayan projelerde, 
    # bu tarz kisa cozumler ozellikle zamandan tasarruf edilmesini saglar.
    # once kendin nasil yapabilecegini dusun, sonra en sonda ekledigim kodlardan asagidan kontrol edebilirsin
    letter_list.append(i)  
    count_list.append(count)

letter_dictionary = {letter_list[j]: count_list[j] for j in range(26) if count_list[j] >= 1}  
# creating dictionary and 'if block' is there for elimination of 0 count values. 
# 26 is the number of letters in the alphabet

# bu basamaktan sonrasina da gerek yok aslinda
# letter_dictionary.items() sonucu yine ayni sekilde 'liste' formatinda dondurecektir.
list_letter_dictionary = []  # created this block to see desired output, otherwise the values in the dictionary were printed out in {}. 
for item in letter_dictionary.items():  # dongu elemani olarak 'item' yerine yine 'i' kullanabiliriz, hatta daha iyi olur.
    list_letter_dictionary.append(item)
print(list_letter_dictionary)

'''
https://stackoverflow.com/questions/16060899/alphabet-range-in-python 
Eger alfabeyi otomatik olusturmak istersen bu linkte nasil yapildigini bulabilirsin, 
ama algoritma mantigini pekistirmek ve farkli problemlere kendi cozumumuzu bulabilmek icin algoritma kurmak en guzeli.
Algoritma cok guzel, gayet basarili.
'''

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