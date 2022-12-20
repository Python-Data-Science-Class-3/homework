'''
Developer   : Musab SARI
Date        : 13.12.2022

Application : Lucky Numbers

Explanation : Lucky numbers is an application where you can create a list and see the survivors from that list which are called lucky numbers.
Survival process is defined as follows, at the first phase, every second element from the list is removed and at the second phase, every third element is removed
and it goes on like this till there is no possible iteration left.
'''

n = list([x for x in range(1, int(input('Enter the range of your list:')) + 1)])  # to create list 
# List comprehension ile dongu kurma, liste olusturma basarili.
# List comprehension liste olarak doner, tekrar list() icine almamiza gerek yok
# ya da list(range(...)) ile de list comprehension kullanmadan liste olusturabiliriz
print('Your list = ', n)

for i in range(2, len(n)):  
    # i'yi 2den baslattigimiz ve i-1'deki elemani sildigimiz icin
    # bazi dongulerde listenin son elemaninin silinebiliyor ve silinmesi gerekiyorken
    # silinmeden kaliyor. Donguyu ona gore yeniden kurmak gerekiyor 
    
    if i < len(n):
        del n[(i - 1)::(i)]
    else:
        break
# Dongu ve algoritma kurma mantigi guzel, gayet basarili
print('Your lucky numbers = ', n)

'''
guzel, okunakli, anlasilir. Tesekkurler...
'''