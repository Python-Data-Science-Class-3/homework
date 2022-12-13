print ( ''' LÜTFEN DIKKAT!!!
Tas, Kagit, Makas oyununa Hosgeldiniz.
Oyun 10 tekrar oynanacaktir. Kazanirsaniz '1' Puan, Kaybederseniz '0' Puan alacksiniz.
Baslamak icin X Tusuna Basin.
Sansli Olan Kazansin...
''')
import random
elemanlar =["tas", "kagit", "makas"]
tas = elemanlar[0]
kagit = elemanlar[1]
makas = elemanlar[2]


puan_oyuncu = 0
puan_bilgisayar = 0
oyun= 0
while (oyun<=10):
    print("oyun sayisi", oyun)
    oyun+=1
    oyuncu = input("tas? kagit? makas? :")
    bilgisayar = random.choice(elemanlar)

    if (oyuncu== bilgisayar) :
       print("Berabere, tekrar oynayiniz")
    elif((oyuncu == tas) and (bilgisayar ==makas)) or  ((oyuncu == makas)and (oyuncu==kagit)) or ((oyuncu== kagit)and (bilgisayar ==tas)):
      puan_oyuncu+=1
    else :
       puan_bilgisayar+=1
    print("oyuncu:", puan_oyuncu, "bilgisayar:" ,puan_bilgisayar)
    if puan_oyuncu >= 6 and puan_oyuncu <=4 :
        print("TEBRIKLER OYUNU KAZANDINIZ")
    else:
        print("OYUNU KAYBETTINIZ")
       
     
   
