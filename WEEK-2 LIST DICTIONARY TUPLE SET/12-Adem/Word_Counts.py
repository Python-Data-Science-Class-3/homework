#Calculation of letter numbers of the entered sentence
a = str( input("Enter the sentence")).lower()
print (a)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#Search each letter within the alphabet 
for i in alphabet: 
#For not print letters that are not in the entered sentence and take the value "0"
    if a.count(i) > 0:
        print (tuple((i  , a.count(i))))

'''
Cok guzel, gayet basarili bir algoritma.
Sadece bizden beklenen cikti liste icinde demet, o sekilde dondurmemiz daha iyi olurdu.
Aslinda sozluk olusturarak yaparsak dict.items() komutu ile cagirinca liste icinde demet olarak doner.
Biraz daha deneyerek bir sozluk olusturmayi deneyin.
Daha sonra sizin cozumun biraz degistirilmis halini asagida inceleyip deneyebilirsiniz.
Tebrikler...
'''

'''
sozluk = {}
for i in alphabet: 
#For not print letters that are not in the entered sentence and take the value "0"
    if a.count(i) > 0:
        sozluk[i] =  a.count(i)

print(sozluk.items())
'''