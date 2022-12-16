

print("TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİNİZ")



seçenekler=["taş","kağıt","makas"]

a=input("birinci kullanıcı tercihi")
b=input("ikinci kullanıcı tercihi")

if a==b:
    print("Berabere Kaldınız!!!")
elif a==seçenekler[0] and b==seçenekler[1]:
    print("İkinci oyuncu kazandı")
elif a==seçenekler[0] and b==seçenekler[2]:
    print ("Birinci Oyuncu kazandı")
elif a==seçenekler[1]and b==seçenekler[0]:
    print("Birinci Oyuncu kazandı")
elif a==seçenekler[1] and b==seçenekler[2]:
    print("İkinci Oyuncu kazandı")
elif a==seçenekler[2] and b==seçenekler[0]:
    print("İkinci Oyuncu kazandı")
else:
    print("Birinci Oyuncu kazandı")

print("OYUN SONA ERDİ")











