'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Equal Reverse

Explanation : Equal reverse is an application where user inputs range of words with a coma between them to be checked 
if they are equal to their reverse order and outputs True and False boolean values respectively.
'''
a = list(map(str, input('Please enter your words which are going to be checked if they are equal to their reverse with a coma in between them:').split(',')))

reverse_order = lambda x: [print(True) if x[i][:]==x[i][::-1] else print(False) for i in range(len(x))]

reverse_order(a)


"""
Asagida yaptigin islemleri acarak aciklamaya calistim,
iki yerde kisaltmaya ihtiyac duydum.
Birincisi split() kullanimi, bu bize liste dondureceginden tekrar map ile liste olusturmamiza gerek yok.
Ikincisi foksiyon icindeki if-else kullanimi, zaten esitligi kurdugumuzda True ya da False dondureceginden,
if-else kullanmadan direk True ya da False cevabini aliriz.
'musab' == 'basum'  # bu satir bize False olarak geri doner
'madam' == 'madam'  # bu satir da bize True olarak geri doner
Bir husus da, lower() ile stringin harflerini kucultursek, 
buyuk harf girilmesi durumunda (orn: 'Madam' == 'madaM' ---> False)
yanlis degerlendirmemizi onler

"""


"""
inp = input('Please enter your words which are going to be checked if they are equal to their reverse with a coma in between them:')

splitted = inp.split(',')  # split bize stringleri liste olarak donduruyor

# a = list(map(str, splitted))  # Bu isleme gerek yok, yukardaki satir ayni sekilde liste olarak donduruyor.

reverse_order = lambda x: [print(x[i][:]==x[i][::-1]) for i in range(len(x))]  # Zaten True-False dondurecegimiz if satiri kurmadan, direk bu sekilde yazarsak bize True-False olarak donecektir.

reverse_order(splitted)
"""