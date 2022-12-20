
'''
This program generates lucky number
'''

n = int(input("BIr sayi giriniz"))
s = [nmb for nmb in range(1,n)] # liste olusturduk
# print(s)
for k in range(2,10):   
    del s[k-1::k]   # 2 den baslayarak listenin her k. elemanini cikariyoruz
print(s)  # kalan numaralar bizim sansli numaralarimiz