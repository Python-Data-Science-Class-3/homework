weight = int(input("Kilonuzu kg cinsinden giriniz : \n"))
height = int(input("Boyunuzu cm cinsinden giriniz : \n"))

bodyMassIndex = weight/((height/100)**2)
if bodyMassIndex >= 40 :
    print(f"Boy kilo endeksiniz : {bodyMassIndex:.2f} Asiri kilolusunuz !!!  DIKKAT !!!") 
elif bodyMassIndex >= 30 :
    print(f"Boy kilo endeksiniz : {bodyMassIndex:.2f} Obez") 
elif bodyMassIndex >= 25 :
    print(f"Boy kilo endeksiniz : {bodyMassIndex:.2f} Overweight") 
elif bodyMassIndex < 25 :
    print(f"Boy kilo endeksiniz : {bodyMassIndex:.2f} Normal") 
