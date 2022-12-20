#Write a program that takes two inputs; one of them is a list and the other is a number, 
# and returns the list obtained by shifting the elements in the list n places to the right (left) 
# when n is positive (negative). Use wrap-around if an element is shifted beyond the end of the list, 
# then continue to shift starting at the beginning of the list. 
# Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] 
# Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]

'''
Algoritma dogru calisiyor, gayet guzel.

Liste elemani olarak 2 veya daha fazla haneli sayi giremiyoruz. 
Bunu bir while dongusu ile kullanicidan nasil alabiliriz, 
bunu biraz dusunup kendiniz kurmayi deneyin, daha sonra ornek cozumu incelersiniz.
'''

list1 = list(input("Please input a list of items without space between them: "))
n = int(input("Please input a number: "))
u = len(list1)
newlist = ['x' for i in range(u)]                       # to make a default list in the length of list1

print("\n")

for i in range(u):
    newindex = (i + n) % u                              # to reduct the new index with modulus if it is more than the length of our list 
    newlist[newindex] = list1[i]                        # to assign elements to new indexes
print(newlist)

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