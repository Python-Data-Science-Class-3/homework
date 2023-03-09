""" 

Developer : Melih Orhan Yilmaz
Date      : 07.03.2023

Application : API Homework

Explanation : 
    Write a python script that shows the result by taking the date and currency types from the user to learn from the api 
    site below. You can find the currency symbols on the api site.

    api site: https://www.exchangerate-api.com/

    For example, when the user wants to learn the USD/TRY exchange rate at 15/01/2023, 
    the result is : "1 USD is 18.7872 TRY on 15/01/2023."

    If you want you can use try-except to prevent the incorrect inputs.

"""

import requests

#Users can write the code they want in lower case
currency_from = input("Enter the currency code you want to convert from: ").upper()
currency_to = input("Enter the currency code you want to convert to: ").upper()

# try-except for no invalid date
while True:
    date = input('Enter the date in YYYY-MM-DD format: ')
    try:
        year, month, day = date.split("-") #Used split to assign year-month-day variables
        break  
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

apiKey = 'af56f3457808be3d649bcddc'
# To reach the date and base_code desired by the user
url = f'https://v6.exchangerate-api.com/v6/{apiKey}/history/{currency_from}/{year}/{month}/{day}'

response = requests.get(url)

if response.status_code != 200:
    print("Failed to get exchange rate. Please try again.")

else:
    try:
        rate = response.json()["conversion_rates"][currency_to] # Getting currency_to in json
        print(f"1 {currency_from} is {rate} {currency_to} on {date}.")

    except KeyError:
        print("Invalid currency code. Please enter valid currency code.")