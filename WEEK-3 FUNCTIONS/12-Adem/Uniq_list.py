"""Unique elements function
Function is written for filtering and ordering the repeated 
elements in the list entered by the user.
"""


def uniq_element(x):
#Entering list items from the user
    x = (set(input("lütfen liste elemanlarını giriniz"))) 
    return(x)
#sorting and printing filtered elements
print(sorted(uniq_element(x)))


'''
Liste elemanlarini input ile almamiza gerek yok,
herhangi bir listenin sirali bir sekilde elemanlari
isteniyor bizden. Input kullanacaksak da bunu fonksiyon disinda alip,
olusturulan listeyi fonksiyonu tanimladiktan sonra kullanmamiz gerekir.

Fonksiyon icinde degisken tanimlarken dikkat etmemiz gereken konu 
degiskenlerin global ve local variable seklinde iki turlu oldugudur.
Eger bir fonksiyon icinde degisken tanimlarsaniz, bu degisken o fonksiyona ozgu olur, 
ve fonksiyon disinda kullanamazsiniz, kullanmaya calistiginizda su andaki halinde oldugu gibi
hata verir (name 'x' is not defined!), cunku oyle bir variable aslinda globalde yoktur, sadece localde vardir.
Ama global degisken dedigimiz kavram fonksiyon disinda tanimlayip kullandigimiz degiskenlerdir.

Burada x'i fonksiyondan once input seklinde alip ya da kendiniz herhangi bir liste olusturup,
daha sonra fonksiyonun elemani olarak baska bir degisken mesela 'y' gibi bir isim tanimlarsaniz,
bu y uzerinde de fonksiyon icinde set ve sort islemlerini uygular ve return edersek,
daha sonra fonksiyon icinde onceden tanimladigimiz x'i kullandigimizda bize o liste
fonksiyon icinde islemden gecmis bir sekilde donecektir.

return satirini tekrar gozden gecirelim, kullanimi hatali olmus.

En sonda bir cozum sundum, inceleyebilirsiniz.
'''




'''
# Fonksiyon satirlari
def unrepeated(first_list): 
    last_list = sorted(set(first_list))
    return last_list

# liste olusturmak icin kullanicidan while dongusu ile liste elemanlarinin alinmasi
# sizin kullandiginiz metod ile sadece birer haneli elemanlar alabiliyoruz,
# fakat bu sekilde cok sayida haneli elemanlar alabiliriz.

print("Liste olusturmak icin her seferinde eleman girip Enter'a basin, cikis icin 'q' girin")
x = []
while True:
    inp = input('Listeye girmek istediginiz elemani giriniz: ')
    if inp == 'q':
        answer = input('Listeye ekleme islemini sonlandirmak istiyorsaniz "e" (evet), degilse "h" (hayir) yazin: ')
        if answer == "e":
            break
        else:
            x.append(inp)
            continue      
    x.append(inp)

print(unrepeated(x))

'''