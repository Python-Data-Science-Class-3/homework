a=str(input("1.oyuncunun adini giriniz:"))
b=str(input("2.oyuncunun adini giriniz:"))
a_h=str(input(f' {a}: tas  kagit ya da  makas   seceneklerinden birini giriniz:'))   #a_h:a nin hamlesi olsun
b_h=str(input(f' {b}: tas  kagit ya da  makas   seceneklerinden birini giriniz:'))    #b_h:b nin hamlesi olsun
#print(a,"nin hamlesi=",a_h)
#print(b,"nin hamlesi=",b_h)
a_s=0     #a nin baslangic skoru
b_s=0     #b nin baslangic skoru
c_s=0     #beraberlik hali
while ((a_s)+(b_s)+(c_s))<=9:
    if a_h=="tas"and b_h=="kagit":
        print("b kazandi")
        b_s+=1
    elif a_h=="tas"and b_h=="makas":
        print("a kazandi")
        a_s+=1
    elif a_h=="tas"and b_h=="tas":
        print("kimse kazanamadi")
        c_s+=1
    elif a_h=="kagit"and b_h=="tas":
        print("a kazandi")
        a_s+=1
    elif a_h=="kagit"and b_h=="makas":
        print("b kazandi")
        b_s+=1
    elif a_h=="kagit"and b_h=="kagit":
        print("kimse kazanamadi")
        c_s+=1
    elif a_h=="makas"and b_h=="tas":
        print("b kazandi")
        b_s+=1
    elif a_h=="makas"and b_h=="kagit":
        print("a kazandi")
        a_s+=1
    elif a_h=="makas"and b_h=="makas":
        print("kimse kazanamadi")
        c_s+=1

    print(f'a nin skoru={a_s}\nb nin skoru={b_s}\nberaberlik={c_s}\n')

