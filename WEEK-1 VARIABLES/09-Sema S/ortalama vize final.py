
Name =str(input("Adınızı giriniz:"))
Surname =str(input("Soyadınızı giriniz:"))
StudentNumber =int(input("Öğrenci Numaranızı Giriniz:"))

Dersler =[["Topoloji" ,False], ["Analiz" ,False] ,["Cebir" ,False] ,["Sanat" ,False]]



for i in Dersler:
    VizeNotu =input(i[0] +" dersinin Vize Notunu Giriniz:")
    FinalNotu =input(i[0] +" dersinin FinalNotunu Giriniz:")
    Ortalama = float(VizeNotu) * (40 / 100) + float(FinalNotu) * (60 / 100)

    print("Ortalamanız:{}".format(round(Ortalama,2)))


    if Ortalama > 50:
        i[1] = True
for i in Dersler:
    if i[1] == True:
        print(i[0] +" dersinden gectiniz.")
    else:
        print(i[0] +" dersinden kaldiniz.")







