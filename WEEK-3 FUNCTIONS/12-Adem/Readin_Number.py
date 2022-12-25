def reading_number(num):
    empty = ''
    x = [empty, 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',
        'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
        'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
 
    y = [empty, empty, 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
        'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
   

    if (num < 20):
        return x[num]

    if (num < 100):
        return y[num // 10 ] + x[num % 10]
reading_number(25)  # print(reading_number(input(...)))

"""
Oncelikle fonksiyonu return etmemiz demek bize bir cikti saglayacak demek degildir.
Return ile fonksiyon sonucu hafizasina kaydedip bir deger elde ediyor, donduruyor,
fakat bunu yazdirmak istiyorsak print() kullanmamiz gerekir, ya da
baska bir islemde bu sonucu kullanacaksak bir variable'a atayarak ya da herhangi bir yerde fonksiyonu cagirarak
bu degeri kullanabiliriz.
Yani fonksiyonu print icerisinde cagirmamiz gerekir, 
ya da fonksiyondan donen degeri print ile fonksiyon icerisinde tanimlamamiz gerekir.

Ikinci olarak da kullanicidan aldigimiz bir input ile girilen sayiyi okutalim.

Onun disinda algoritma basarili, tebrikler.
"""