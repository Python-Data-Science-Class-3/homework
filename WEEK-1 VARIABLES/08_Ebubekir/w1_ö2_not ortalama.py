
name=input("adinizi yaziniz:")
surname=input( "soyadinizi yaziniz:")
student_number=input("ogrenci numaranizi giriniz:")
vize1=int(input("ders1 vize notunuzu giriniz:"))
vize2=int(input("ders2 vize notunuzu giriniz:"))
vize3=int(input("ders3 notunuzu giriniz:"))
vize4=int(input("ders4 vize notunuzu giriniz:"))
final1=int(input("ders1 final  notunuzu giriniz:"))
final2=int(input("ders2 final  notunuzu giriniz:"))
final3=int(input("ders3 final  notunuzu giriniz:"))
final4=int(input("ders4 final  notunuzu giriniz:"))

"""for i in range(1,5): # 4 ders girilecek
    ders = input(f"\n{i}. Dersin Adını Girin : ")
    vize = float(input(f"{i}. Dersin Vize Notunu Girin : "))
    final = float(input(f"{i}. Dersin Final Notunu Girin : "))"""


"""ortalama1=round(vize1*40/100+final1*60/100,2)
ortalama2=round(vize2*40/100+final2*60/100,2)
ortalama3=round(vize3*40/100+final3*60/100,2)
ortalama4=round(vize4*40/100+final4*60/100,2)"""

ortalama1=vize1*40/100+final1*60/100
ortalama2=vize2*40/100+final2*60/100
ortalama3=vize3*40/100+final3*60/100
ortalama4=vize4*40/100+final4*60/100

"""print("1.dersin ortalamasi=",ortalama1,"\n2.dersin ortalamasi=",ortalama2,
      "\n3.dersin ortalamasi=",ortalama3,"\n4.dersin ortalamasi=",ortalama4)"""

print("--------------")
print("--------------")
print(f'sayin {student_number} numarali {name} ')
if ortalama1<50:
    print(f'1.dersin ortalamasi={ortalama1:.2f}---->ders1= FAILED')
else:
    print(f'1.dersin ortalamasi={ortalama1:.2f}---->ders1= PASSED')
print("--------------")
if ortalama2 < 50:
    print(f'2.dersin ortalamasi={ortalama2:.2f}---->ders2= FAILED')
else:
    print(f'2.dersin ortalamasi={ortalama2:.2f}---->ders2= PASSED')
print("--------------")
if ortalama3<50:
    print(f'3.dersin ortalamasi={ortalama3:.2f}---->ders3= FAILED')
else:
    print(f'3.dersin ortalamasi={ortalama3:.2f}---->ders3= PASSED')
print("--------------")
if ortalama4 < 50:
    print(f'4.dersin ortalamasi={ortalama4:.2f}---->ders4= FAILED')
else:
    print(f'4.dersin ortalamasi={ortalama4:.2f}---->ders4= PASSED')

