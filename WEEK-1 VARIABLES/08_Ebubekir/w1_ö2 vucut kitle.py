while True:

 boy=float(input("boyunuzu metre cinsinden giriniz="))
 kilo=float(input("kilonuzu kg cinsinden giriniz="))
 vke=kilo/(boy**2)    #vke=vucut kite endeksi,2
 print(f'vucut kitle endeksiniz={vke:.2f}')
 if vke<=25:
     print("NORMAL")
 elif 25<=vke<30:
     print("OVER WEIGHT")
 elif 30<=vke<40:
     print("OBSE")
 else:
    print("EXTREMELY OBSE")

"""while True:

 boy=float(input("boyunuzu metre cinsinden giriniz="))
 kilo=float(input("kilonuzu kg cinsinden giriniz="))
 vke=round(kilo/(boy**2),2)#vke=vucut kite endeksi,2
 print("vucut kitle endeksiniz=",vke)
 if vke<=25:
     print("NORMAL")
 elif 25<=vke<30:
     print("OVER WEIGHT")
 elif 30<=vke<40:
     print("OBSE")
 else:
    print("EXTREMELY OBSE")
#30dk    """