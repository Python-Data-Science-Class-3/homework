Kilo = float(input("Kilonuzu Yaziniz:"))
Boy =  float(input("Boyunuzu Yaziniz:"))
Endeks= Kilo / (Boy*Boy)
print("Endeks:", Endeks)

if (Endeks < 25) :
    print("NORMAL")
elif Endeks >= 25 and Endeks <30 :
    print("ASIRI KILO")  
elif  Endeks >=30 and Endeks <40 :
    print("OBEZITE") 
elif Endeks >=40 :
    print("ASIRI OBEZITE")     