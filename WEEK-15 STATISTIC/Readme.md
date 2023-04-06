# Class 3 Week 15 Statistic Homework

"""

### DATASET:Asagidaki df'i dataset olarak kullanabilirsiniz.


#### import numpy as np


#### import pandas as pd


#### # 100 ürün oluşturun**


#### n = 100


#### # Rastgele fiyatlar oluşturun


#### prices = np.random.normal(50, 10, n)


#### # Rastgele bir iade olasılığı oluşturun


#### return_prob = np.random.uniform(0, 1, n) #100 adet 0 ila 1 arasinda rastgele oran olusturur


#### # İade edilip edilmediğini belirleyin


#### # NOT: Urun degerlendirme Yuzdesinde %20 altindakilerin iade edildigi seklinde bir limit belirledik, ve datamizi simule ettik.


#### returns = return_prob < 0.2


#### # Veri çerçevesini oluşturun


#### df = pd.DataFrame({'Price': prices,'Urun_Degerlendirme_Oran':return_prob ,'Return': returns})


### SORULAR


1. Verilen bir ürünün fiyatı 50-70 aralığındaysa, ürünün geri dönüş olasılığı nedir?

2. Ürün değerlendirme oranı 0.5'ten büyük olan bir ürün alındığında, fiyatının 30-50 aralığında olma olasılığı nedir?

3. Bir ürünün fiyatı 50-70 aralığındaysa, ürün değerlendirme oranı 0.5'ten büyük olduğunda geri dönüş olasılığı nedir?

4. Bir ürünün fiyatı 70'den fazla olduğunda, ürün değerlendirme oranı 0.5'ten büyük olma olasılığı nedir?


### Bayes Rule Question:


5. Dört şeritli bir otoyolda arabalar ya hızlı gidiyor ya da hızlı gitmiyor. Daha hızlı arabalar en sol şeritte gitmelidir. Herhangi bir zamanda, arabaların %20'si en soldaki şerittedir. Genel olarak, otoyoldaki arabaların %40'ı hızlı gidiyor olarak sınıflandırılır. Tüm arabaların içinde, en soldaki şerittekilerin %90'i hızlı gidiyor. Bir araba hızlı gidiyorsa, En Soldaki Şeritte olma olasılığı nedir?

"""
