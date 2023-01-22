gamer_1 = input("Lütfen ilk oyuncunun ismini girin: ")
gamer_2 = input("Lütfen ikinci oyuncunun ismini girin: ")

score_1 = 0
score_2 = 0

print ("Oyuna baslamak icin tas (T), kagit(K) veya makas(M) arasindan secim yapiniz..")
while True:
    for i in range(1,11):
        print(f"{i}. el:")
        chose_1 = input(f"{gamer_1}: ").upper()
        chose_2 = input(f"{gamer_2}: ").upper()
        if (chose_1 == "T" and chose_2 == "K") or (chose_1 == "K" and chose_2 == "M") or (chose_1 == "M" and chose_2 == "T"):
            score_2 += 1
        elif (chose_1 == "T" and chose_2 == "M") or (chose_1 == "K" and chose_2 == "T") or (chose_1 == "M" and chose_2 == "K"):
            score_1 += 1
        elif (chose_1 == "T" and chose_2 == "T") or (chose_1 == "K" and chose_2 == "K") or (chose_1 == "M" and chose_2 == "M") :
            continue
        else:
            print("Hatali giris..")
        print(f"{gamer_1} : {score_1}       {gamer_2} : {score_2} ")
    while i == 10:
        if (score_1 > score_2):
            print(f"Oyun sona erdi.. Kazanan oyuncu {gamer_1}")
        elif (score_1 < score_2):
            print(f"Oyun sona erdi.. Kazanan oyuncu {gamer_2}")
        else:
            print("Oyun berabere bitti..")
        quit()
