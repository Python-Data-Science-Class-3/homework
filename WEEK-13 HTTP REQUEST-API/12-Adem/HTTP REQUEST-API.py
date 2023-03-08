import requests
from datetime import datetime

date = input('Enter date in format YYYY/MM/DD: ')
currency_from = input('Enter the currency code to convert from (e.g. USD): ').upper()
currency_to = input('Enter the currency code to convert to (e.g. TRY): ').upper()
#apiKey = 'ea04934fa06c37f6e846ee5d'

def rate(date, currency_from, currency_to):
    url =f"https://v6.exchangerate-api.com/v6/ea04934fa06c37f6e846ee5d/history/{currency_from}/{date}"

    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        target_rate = data["conversion_rates"][currency_to]
        return f"1 {currency_from} is {target_rate} {currency_to} on {date}."
    else:
        return "Error: Unable to retrieve exchange rate information."
    
try:
    result = rate(date, currency_from, currency_to)
    print(result)
except:
    print("Error: Invalid input.")