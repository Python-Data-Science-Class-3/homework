import requests

apiKey = '10a257b790a0ba092edfe206'  #siteye girip login olunca get api key diyerek aliyoruz bu key i
url ='https://v6.exchangerate-api.com/v6/10a257b790a0ba092edfe206/latest/USD'

response = requests.get(url)
data=response.json()
print (data)
kur = data['conversion_rates']['TRY']
miktar=int(input('kac dolar cevirmek istiyorsunuz?'))
top=miktar*kur
print(50*'-')
print(f"1 $= {kur} TRY")
print(50*'-')
print(f'{miktar}$={top} TRY')
