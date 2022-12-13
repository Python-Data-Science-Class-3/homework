

secenek = ["taş", "kağıt", "makas"]
taş = secenek[0]
kağıt = secenek[1]
makas = secenek[2]
oyuncu1_skor = 0
oyuncu2_skor = 0
print("Taş,kağıt,makas oyununa hoş geldiniz.")

while True:
    oyuncu1_secim = input("OYUNCU1 tas mi,kagit mi,makas mi")
    oyuncu2_secim = input("OYUNCU2 tas mi,kagit mi,makas mi")

    if  oyuncu1_secim == "taş":
        if oyuncu2_secim == "taş":
            print("Berabere")
        elif oyuncu2_secim == "makas":
            oyuncu1_skor = oyuncu1_skor + 1
            if oyuncu1_skor == 5:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                
                break
            else:
        
                print("oyuncu1_skor: {} , oyuncu2_skor : {}\n".format(oyuncu1_skor, oyuncu2_skor))

        else:
            oyuncu2_skor = oyuncu2_skor + 1
            if oyuncu2_skor == 5:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                print("Oyun bitti. oyuncu1 Kaybetti...")
                break
            else:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                
    elif oyuncu1_secim == "kağıt":
        if oyuncu2_secim == "kağıt":
            print("Berabere")
        elif oyuncu1_secim == "taş":
            oyuncu1_skor = oyuncu1_skor + 1
            if oyuncu1_skor == 5:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
              
                break
            else:
                
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))

        else:
            oyuncu2_skor = oyuncu2_skor + 1
            if oyuncu2_skor == 5:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                
                break
            else:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                

    elif oyuncu1_secim == "makas":
        if oyuncu2_secim == "makas":
            print("Berabere")
        elif oyuncu2_secim == "kağıt":
            oyuncu1_skor = oyuncu1_skor + 1
            if oyuncu1_skor == 5:
               print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
            
               break

            else:
            
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
        else:
            oyuncu2_skor = oyuncu2_skor + 1
            if  oyuncu2_skor == 5:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
                break
            else:
                print("oyuncu1_skor: {} , oyuncu2_skor: {}\n".format(oyuncu1_skor, oyuncu2_skor))
    
            break