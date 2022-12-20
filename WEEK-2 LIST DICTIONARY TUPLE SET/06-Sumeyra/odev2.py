# Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). 
# Use wrap-around if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list. 
# Example Inputs [1, 2, 3, 4, 5], 2 
# Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]
'''
Bu sekilde de yorum satirlari kullanabilirsiniz,
ozellikle bu gibi aciklama kisimlarinda... (Yukaridaki aciklamalara atfen bahsettim)

Yazim usullerine, aralik birakilmasi gereken yerlerde aralik birakmaya biraz daha ozen gosterirseniz
daha guzel olur, oyle de olmasi gerekir. Bunlarin bir standardi var, PEP 8 - Style Guide for Python.
https://peps.python.org/pep-0008/#comments dilerseniz bu linkten inceleyebilirsiniz.

2 ya da daha fazla haneli sayi girmemiz gerektiginde listeyi nasil olusturacagiz?
Sizin cozumunuzde girdiginiz sayinin tum hanelerini listenin elemani olarak almissiniz.


Liste uzunlugundan daha buyuk kaydirma yapamiyoruz, bunu yapmak icin mod kullanmamiz gerekir.

En sonda bir cozum var, donguleri nasil kullandigimizi lutfen ordan dikkatle inceleyin,
bu tarz donguler kullanmak icin kendinizi zorlayin. Bu sekilde pratiklerle ogrendikleriniz birikerek gelisir.
'''

nums1 = list(input("enter list elements")) 
print(nums1)
n = int(input("enter a number")) 
nums2 = nums1[-n:] + nums1[:-n]  # how much displacement is desired, it divides and then joins the pieces
print(nums2)


'''
print('\nListe olusturmak icin her seferinde entera basarak listeye birer birer sayi ekleyin,\nlisteyi olusturduktan sonra "Q"ya basarak islemi kapatin\n')

list_1 = []
while True:
    
    inp_1 = input('Lutfen sayi girin: ')
    
    if inp_1 == 'q' or inp_1 == 'Q':
        break
    
    list_1.append(int(inp_1))
    

print(list_1)


while True:
    
    inp_2 = input("Listeyi kaydirmak istedigin miktari ve yonunu sec (sola ise -, saga ise + deger gir) \n(programi sonlandirmak icin 'Q'ya basin): ")
    
    if inp_2.lower() == 'q':
        break
        
    list_2 = list_1.copy()
    for i in range(len(list_1)):
        list_2[(int(inp_2)+i) % len(list_1)] = list_1[i]
        
    print('Ilk liste: ', list_1)
    print('Son liste: ', list_2)
'''