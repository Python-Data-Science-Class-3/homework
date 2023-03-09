import requests

url = 'https://v6.exchangerate-api.com/v6/07700d3b38e48b6108120715/latest/USD'
response = requests.get(url)#, params={
    # base_code:'USD'})
print(response)
data = response.json()
currencyList =[]
for i in data['conversion_rates'].keys():
    currencyList.append(i)
print(currencyList)
while True:
    baseCode= input("enter a currency code abobe1 : ").upper()
    url2 = f'https://v6.exchangerate-api.com/v6/07700d3b38e48b6108120715/latest/{baseCode}'
    # print(data['conversion_rates'].keys())
    response2 = requests.get(url2)
    data2 = response2.json()

    currency2 = input("enter a valid currency above above: ").upper()

    print(data['conversion_rates'][currency2])
