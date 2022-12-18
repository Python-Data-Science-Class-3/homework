kelime1=input("bir kelime giriniz:")
kelime2=input("başka bir kelime daha giriniz:")

a=set(kelime1)
b=set(kelime2)


for  kelime in a and b:
    x =sorted(list(a.intersection(b)))
    y=sorted(list(a.difference(b)))
    z=sorted(list(b.difference(a)))
if x!=0 and y!=0 and z!=0:

    print(["".join(x),"".join(y) ,"".join(z)])