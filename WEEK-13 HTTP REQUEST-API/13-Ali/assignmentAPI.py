import requests

url = 'https://v6.exchangerate-api.com/v6/07700d3b38e48b6108120715/history/USD/2023/01/25'
response = requests.get(url)#, params={
    # base_code:'USD'})
print(response)
data = response.json()
# print(data)
currencyList =[]
print("CURRENCY BASE CODES LIST YOU CAN USE YOUR REQUEST")
for i in data['conversion_rates'].keys():
    currencyList.append(i)
print(currencyList)


while True:
    baseCode= input("enter a currency code abobe1 : ").upper()
    year= input("enter year : ")
    month= input("enter month: ")
    day= input("enter day : ")
    url2 = f'https://v6.exchangerate-api.com/v6/07700d3b38e48b6108120715/history/{baseCode}/{year}/{month}/{day}'
    # print(data['conversion_rates'].keys())
    response2 = requests.get(url2)
    data2 = response2.json()
    currency2 = input("enter a valid currency above above: ").upper()
    print(data['conversion_rates'][currency2])
