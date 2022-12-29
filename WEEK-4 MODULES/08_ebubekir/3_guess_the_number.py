import random,time,os
pc_tahmin=random.randint(1,100)
tur_sayaci=0
timer=time.localtime(time.time()).tm_sec
while True:
    tahmin=int(input("1 ile 100 arasinda bir sayi giriniz:"))
    tur_sayaci+=1
    if tahmin<pc_tahmin:
        print("↑ ↑ ↑ ↑ ↑ ")
        
    elif tahmin>pc_tahmin:
        
        print("↓ ↓ ↓ ↓ ↓")
        
    elif tahmin==pc_tahmin:
        break    
os.system('cls')
print("Tebrikler {} denemede ve {} saniyede tahmin ettiniz:".format(tur_sayaci,timer))    