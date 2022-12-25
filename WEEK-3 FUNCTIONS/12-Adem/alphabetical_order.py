#ALPHABETİCAL_ORDER
def alp_order():
    alp_order = (list(input("Enter elements with \"-\" sign between them.").split("-")))
    alp_order.sort()
    return ('-'.join(alp_order))
alp_order()

"""
alp_order() burada bizim "function_name" yani fonksiyon adimiz.

Fonksiyon'un bir de parametre almasi gerekir ("parameter"), 
burasi bizim kodumuzda parantez icerisindeki kisim, bos birakilmis.

Daha sonra fonksiyonun icinde "Four-space margin (4 bosluk)" birakilarak "Function body" olusturulur.
Bu yapi icerisinde de fonksiyondan ne bekledigimizi, nasil islem yapmasi gerektigini ve en sonda da print()
ya da return ... ile ne bekleniyorsa bunu belirtiriz.
split ve sort islemlerini yapip return aldigimiz kisim burasi.

Daha sonraki adimlarda ise herhangi bir argument ile fonksiyon cagrilarak islem yapmasini bekleriz.

Size ornek bir cozum gonderdim, duzeltmeye calistiktan sonra onu incelersiniz.

Bir de sort() ile sorted() farkina bakabilirseniz sevinirim.

"""
"""
# kelimeleri sirasiyla input ile kullanicidan aliriz
words_input = input("Please enter different words with hyphen (-) in between them:")

# fonksiyon icerisinde 'words' parametresi uzerinde islem yaparak 'words1' local degiskenini elde edip
# bunu print ettiririz.
def alp_order(words):
    words1 = "-".join(sorted(words.split("-")))
    print(words1)

# fonksiyonumuzu en basta kullanicidan aldigimiz kelimeler ile cagiralim 
alp_order(words_input)
"""
