3.
"""
Write a code snippet that inputs a sentence from the user,
then uses a dictionary to summarize the number of occurrences of each letter.
Ignore case, ignore blanks and assume the user does not enter any punctuation.
Display a two-column table of the letters and their counts with the letters in sorted order. 
Example Input This is a sample text with several words 
This is more sample text with some different words Output
[('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4),
 ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
"""
sentence=input("write a sentence with no spaces between words and no punctuation marks:")
count_1=dict()
harf=[]
for x in sentence:
    harf.append(x) #
    if x in count_1:   #1 tane varsa 1 yaz daha fazlaysa say
        count_1[x]+=1
    else:
        count_1[x]=1
print(count_1)
count_1.items()   #sozlukteki key ve value degerlerini birlikte almak icin
list(count_1.items())  #bunlari listeye cevirdik
print(list(count_1.items()))
