#Write a programme to generate the lucky numbers from the range(n). 
# These are generated starting with the sequence s=[1,2,...,n]. 
# At the first pass, we remove every second element from the sequence, resulting in s2.
# At the second pass, we remove every third element from the sequence s2,resulting in s3, and we proceed in this way until no elements can be removed. 
#The resulting sequence are the numbers lucky enough to have survived elimination. The following example describes the entire process for n=22 
#Original sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] Remove 2nd elements [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
#Remove 3rd elements [1, 3, 7, 9, 13, 15, 19, 21] 
# Remove 4th elements [1, 3, 7, 13, 15, 19] 
# Remove 5th elements [1, 3, 7, 13, 19] 
# We cannot remove every other 6th element as there is no 6th element. 
# Input 22 Output Lucky numbers are [1, 3, 7, 13, 19]


n = int(input("Enter number: "))
list = [i+1 for i in range(n)]  # list, liste olustururken kullandigimiz komuttur, 
                                # o sebeple variable olustururken list yerine list1, list_1, liste, ...vs
                                # gibi uygun isimler kullanmaniz daha iyi olur
print(list)

for num in range(n):
   if num >= len(list)-1:  # If num is equal to the length of the list, the loop stops
      break
   del list[num+1:n:num+2]  # indexes are deleted
   print(list)  # Sadece son kalan listemizi print ettirsek yeter. Butun asamalari print ettirmeye gerek yok.

'''
Algoritma basarili.

Dongulerde, if ifadelerinde, icice gecen satirlarda arada birakilan 'indent' diye adlandirilan bosluklari
dogru hizalamamiz onemli, normalde Shift ile kaydirinca otomatik olarak bir sonraki kademeye gecer ya da
for veya if satirinin sonundaki : kullanimindan sonra Enter ile alt satira gecerken
otomatik olarak o boslugu kod derleyici kendi ayarlar.
PyCharm 4, Spyder, Jupyter Notebook gibi IDE'ler 4 bosluk birakiyor, bu ayarlanabiliyor da.
VS Code 3 bosluk birakiyor, bu da ayarlaniyordur belki, bilmiyorum. Python standart yaziminda
syandart 4 bosluktur, ama onemli olan kac bosluk oldugundan ziyade her kademenin hizali olmasidir.
Aksi takdirde hatali sonuclar olacaktir. Burdaki bir alt kademeye gecis boslugunu buyuk bir listede
icice gecmis baska bir liste gibi, ya da uzun bir parantezde icte bir parantez daha acmak gibi dusunebilirsiniz.
Nitekim for dongusunun icindeki print komutunu da dusunursek, bir ust kademeye gectiginde 
for dongusunden cikmis olup ana kod satiri ile eslesecektir.
Bu konu ozellikle icice gecen karmasik dongulerde ya da fonksiyonlarda, veya kosullari kullanirken,
neyi nerde nasil kullanacagimizi gorsel olarak da algilamamizi kolaylastiran ve o sekilde
kullanilmasi gereken onemli yazim kurallaridir.

'''
