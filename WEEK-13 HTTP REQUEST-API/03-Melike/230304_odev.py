""" Write a python script that shows the result by taking the date and currency types from the user to learn from the api site below. 
You can find the currency symbols on the api site. api site: https://www.exchangerate-api.com/

For example, when the user wants to learn the USD/TRY exchange rate at 15/01/2023, the result is : "1 USD is 18.7872 TRY on 15/01/2023."
If you want you can use try-except to prevent the incorrect inputs."""

import requests

print("\nWelcome!! Please input the related date and currencies to find base rate of a currency\n ")

while True: 
    try:
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")

        first = (input("\nPlease input base currency: ")).upper()
        second = (input("Please input a currency to convert: ")).upper()

        apiKey = 'd65c90dc66e1f6a96333c3bd'
        url = f'https://v6.exchangerate-api.com/v6/{apiKey}/history/{first}/{year}/{month}/{day}'

        response = requests.get(url)

        result = response.json()['conversion_rates'][second]

        print(f"\n1 {first} is {result} {second} on {day}/{month}/{year}")
    
    except:
        print("Non-acceptable API request, please input a valid date and currency..\n")