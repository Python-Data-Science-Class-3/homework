'''
Gayet guzel, ama bizden istenen bir liste icerisinde
bunlari string olarak dondurmek.
Yani sorted() isleminden sonra ''.join() ile string olusturmak.
Daha sonra bu stringleri bir listede toplayip,
sadece bu listeyi yazdirmak yeterli.
Once kendiniz yapmayi deneyin, daha sonra en sondaki
ornek koda bakabilirsiniz

'''




# Find common letters of 2 entered words.
a = str(input("Enter the first word: ")).lower()
b = str(input("Enter the second word: ")).lower()
print(a)
print(b)
#If the user enters any character other than the letter, they will get a warning
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in (a and b) :
        if i not in list(alphabet):
            print(f"Incorrect entry!!! Please use only letters.\n First Word= {a}\n Second Word = {b}")
#converting sets into lists
intersection = (list(set(a) & set(b)))
a_b = (list(set(a) - set(b)))
b_a = (list(set(b) - set(a)))
# ordering list elements
intersection.sort()
a_b.sort()
b_a.sort()
print(intersection)
print(a_b)
print(b_a)





'''
ortak  = (''.join(sorted(list(kelime_1 & kelime_2))))
fark1 = (''.join(sorted(list(kelime_1 - kelime_2))))
fark2 = (''.join(sorted(list(kelime_2 - kelime_1))))

outputs = [ortak, fark1, fark2]

print(list_of_outputs)
'''