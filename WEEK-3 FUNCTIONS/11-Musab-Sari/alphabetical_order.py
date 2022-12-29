'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Alphabetical Order

Explanation : Alphabetical order is an application where user can enter multiple words at the same time with a '-' between them and outputs sorted
version of the same items in the list with '-' in between them.
'''
alphabetical_order = lambda x = sorted(map(str, input('Please enter your words with an expression "-" in between them:').split('-'))): print('-'.join(x))

alphabetical_order()


"""
lambda kullanmaya calisman guzel, fakat biraz garip bir kullanim olmus.
Normalde lambda X: ... seklinde fonksiyonu kurariz,
ama burda fonksiyonun sonuucunu argumani olarak belirtmissin.
Normalde inputu disardan global bir degiskene atayip, 
daha sonra fonksiyonun argumanlari ve islevini tanimlayip,
en sonunda fonksiyona bu global degiskeni atayarak islemden geciririz.
Fonksiyon icinde inputu alip sonuc da dondurebiliriz.
Ama senin yaptigin cozumde fonksiyona sabit bir arguman gondermis gibi oluyor,
asagida ayni fonksiyonu def ile kurmaya calisarak aciklamaya calistim.
Sonrasinda da fonksiyonu nasil kurarizi gostermeye calistim.
"""


"""
# lambdayi senin kullandigin sekil:

def alphabetical_order(x = sorted(map(str, input('Please enter your words with an expression "-" in between them:').split('-')))):
    print('-'.join(x))

alphabetical_order()
"""

"""
# fonksiyonun dogru kurulumu:

inp = input('Please enter your words with an expression "-" in between them:')

def alphabetical_order(x):  # burda x argumani olarak inputtan gelen stringi fonksiyona sokuyoruz
    y = sorted(map(str, x.split('-')))  # burda fonksiyona string olarak giren x inputunu, sirali kelimeler sekilde y listesi haline getiriyoruz
    x = '-'.join(y)  # burda ise y listemizi aralarinda - olacak sekilde tekrar string haline getiriyoruz ve yine x local degiskenine atiyoruz
    print(x)

alphabetical_order(inp)  # fonksiyonu inputumuz ile cagiriyoruz
ok
"""