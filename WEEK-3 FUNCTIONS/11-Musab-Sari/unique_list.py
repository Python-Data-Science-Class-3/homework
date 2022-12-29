'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Unique List

Explanation : Unique list is an application where user enters items in a list and outputs unique items which do not repeat itself in that list.
'''

a = list(input('Please enter your list with a space between:').split(' '))
 
def unique_list(x):
    
    k = set()
    [k.add(x[i]) for i in range(len(x))]
    print(list(k))

unique_list(a)

"""
equal_reverse odevindeki yorumlarda da belirttigim gibi, 
split() bize stringi liste seklinde donduruyor,
o yuzden tekrar list() komutuna ihtiyacimiz yok. 
Liste olusturmak icin sagidaki satir yeterli:

a = input('Please enter your list with a space between:').split(' ')

Soruda liste seklinde fonksiyona arguman istemis, yani liste girip liste cikacak sekilde,
bu acidan senin cozumun dogru. Ayrica input ile almana da gerek yoktu ama sorun yok, iyi de olmus,
ne kadar cok kullanirsak o kadar pekisir.
Bilgi olmasi acisindan fonksiyonun argumani string de olabilir, 
yani split islemini fonksiyon icinde de tanimlayabilirsin.
Yani fonksiyona giren veri tipi String, fonksiyondan cikan veri tipi Liste seklinde olabilir.
(Sadece input girilip, kalan butun islemler fonksiyondan gecirilecek sekilde yani.)
Bizden istenmemis ama sorted() ile siralayarak daha guzel bir sunum da yapabiliriz. 

Gayet guzel, tebrikler..
ok
"""