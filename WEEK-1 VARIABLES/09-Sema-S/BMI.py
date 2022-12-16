



boy=int(input("Boyunuzu giriniz(cm cinsinden): "))
kilo=int(input("Kilonuzu giriniz(Kg cinsinden): "))
BMI=float(kilo/((boy/100)**2))
print("Vücut kitle index'iniz {}".format(round(BMI,2)))
print("Durumunuz: ")
if BMI <=25:
    print("NORMAL")

elif 25< BMI<=30:
    print("OVER WEIGHT")
elif 30<BMI<40:
    print("EXTREMELY OBSE ")

else:
    print("WARNING,You are very overweight!!!!!!")















