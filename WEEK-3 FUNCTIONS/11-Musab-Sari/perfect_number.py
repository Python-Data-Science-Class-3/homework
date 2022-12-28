'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Perfect Number

Explanation : Perfect number is an application where you can enter a range where your perfect numbers are to be searched. Perfect number is meaning that
a number which equals to sum of its divisors except the number itself.
'''
from functools import reduce

a = int(input('In what range would you like your perfect number to be searched:'))
k = []

def perfect_number(x):
    t = []
    [t.append(y) for y in range(1,a) if x%y == 0 and x != y]
    
    if sum(t) == x:
        
        k.append(x) 
        return  # neyi return ediyoruz?

for i in range(6,a+1):
    perfect_number(i)

print('\nPerfect numbers in the range you setted are:', k)

new_list = filter(lambda x: x<1000, k)
print('\nThe sum of perfect numbers in the range of 1000 is:', reduce(lambda x,y:x+y, new_list))
print('\nIf your range is lower than 1000 then you will see the sum up to your range!')


"""
program basarili calisiyor,
istenen sonucu veriyor,
fakat tam olarak olani soyle aciklayim:

Fonksiyon disinda bir global degisken, bos bir k listesi olusturmusuz.
Daha sonra fonksiyonu cagirinca k listesine islem olarak atama yaptigi icin,
k listemiz istedigimiz gibi doluyor. Bunu print ile cagirinca da tabiiki k listesi geliyor.
Fakat bunun fonksiyonumuz ile bir ilgisi yok, fonksiyonumuz bir islem dondurmuyor.
return satirini bos birakmisiz, hic yazmasak da olurdu. Fakat bu durumda fonksiyon kullanmamiza gerek kalmaz.
Elbette sonradan cagiracagimiz bir durumda isimize yarayacaktir,
fakat fonksiyonu efektif kullanmis olmuyoruz.
Reduce ve Filter islemlerini fonksiyon icinde yapip geri dondurebiliriz,
sadece listeleri donduren ve sadece toplamini donduren ayri birer fonksiyon yazabiliriz.
Ya da her ikisini birden ayni fonksiyonda tanimlayip, ikisini birden tek return ile dondurebiliriz.

variable isimlerini daha belirgin verelim,
t = [], neden t, bu satirda ne yapmaya calisiyoruz, acikca belirtelim. (neden 'divisors' degil mesela)
k = [], neden k (neden 'perfect_nums' degil mesela)
a = input(...) (neden inp degil, ya da daha belirgin bir sey)
perfect_number(x) (neden x, neden 'setted_range' degil)
kodu okurken her seferinde donup bu neydi, su neydi demek ve tekrar bastan okumak durumunda kaliyorum,
o yuzden karsidaki kisinin anlayacagi sekilde acikca isimler secmek en guzeli.

Program bizden herhangi bir input istemiyor, sadece 1 ile 1000 arasindaki perfect sayilari bulup,
bunlarin toplamini istiyor. O yuzden kullanicinin range belirlemesine gerek yok. 
Belirlese bile (10.000 belirleyerek denedim!) 1000'e kadar kisit getirilmis,
arkada hesaplama yapmasi icin bosuna 5-10 sn geciyor.
yani aldigimiz input yerine sadece 1000 yazalim, oyle devam edelim.
Bu durumda girilecek sayiyi arguman alarak onden bir fonksiyon yazip,
bu fonksiyon ile sayinin mukemmel olup olmadigini belirleyebiliriz.
Daha sonrasinda filter ile 1000'e kadar olan sayilari bu fonksiyon ile tarayip,
True olanlari dondurebiliriz. Reduce metodu ile de toplama yapabiliriz.

Bir ornek paylasiyorum, kolay gelsin.






"""

"""
from functools import reduce

# whether it's a perfect number (returns True or False)
def perfect_number(num):
    sum_num = 0
    for i in range(1, num):
        if num%i == 0:
            sum_num += i
    return sum_num == num

# to find the sum of the perfect numbers between 1 and 1000
# perf_nums_list = list(filter(perfect_number, range(1, 1001)))
sum_perf_list = reduce(lambda x, y: x+y, perf_nums_list)
print(sum_perf_list)
"""