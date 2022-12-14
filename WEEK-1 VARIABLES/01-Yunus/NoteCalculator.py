userName = input("Kullanici adi : \n")
userSurname = input("Kullanici soyadi : \n")
coursePassed = 0
for i in range(1,5):
    course1 = input(f"{i}. ders ismi\n")
    not1VIsa = int(input("Vize notunu giriniz : \n"))
    not1Final = int(input("final notunu giriniz : \n"))

    ortalama = not1VIsa*4/10 + not1Final*6/10
    print(f"ortalama notunuz = {ortalama:.2f}  \n")
    if ortalama >= 50 :
        print(f"{course1} basari ile gectiniz\nTebrikler {userName}\n")
        coursePassed += 1
    else :
        print(f"{course1} dersinden kaldiniz\n")

print(f"Gectiginiz ders sayisi {coursePassed}")
if coursePassed >= 2 :
    print("genel olarak basaraili")
else :
    print("basarisiz bir donem... \ndonemi tekrar edin")