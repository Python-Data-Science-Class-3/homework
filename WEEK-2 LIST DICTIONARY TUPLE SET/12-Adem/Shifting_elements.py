'''
1) S-num icin neden yeniden input aldiniz, sanirim shift icin demek istediniz,
giris yaparken kafa karistirici oluyor.

2) Shift islemi yapiyor fakat, algoritma yanlis olmus,
kod dogru cikti vermiyor.

3) Size ornek bir cozum gonderdim, ordan inceleyebilirsiniz.
Kolay gelsin.
'''


"""Program for shifting elements in a list. The user will be entered for the 
   highest element of the list. Shifting number will be entered"""
S_list = int(input("Enter the upper limit of the lucky numbers"))
S_num = int(input("Enter the upper limit of the lucky numbers"))
#making list
S_list = [i for i in range(1,S_list+1)]
print (S_list)
#Warn when the scroll number is more than the number of elements of the list
if S_num >= len (S_list):
        print("The shifting number cannot be same or more from the number of elements of the list. Try again")
        print("Number of elements of the list :", len(S_list))
        print("Number of shifting :",S_num)
else: #shifting numbers with slicing method
    S_list = S_list[S_num:] + S_list[:S_num] 
    print(S_list)


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