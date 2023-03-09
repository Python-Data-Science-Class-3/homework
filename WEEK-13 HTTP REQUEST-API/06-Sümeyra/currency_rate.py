"""Question:

NOTICE : YOU DO NOT NEED TO PAY TO THE API SITE. API site provides this service for a fee. But it can also be done with a 2-week PRO trial account.

Write a python script that shows the result by taking the date and currency types from the user to learn from the api site below. You can find the currency symbols on the api site.

api site: https://www.exchangerate-api.com/

For example, when the user wants to learn the USD/TRY exchange rate at 15/01/2023, the result is : "1 USD is 18.7872 TRY on 15/01/2023."

If you want you can use try-except to prevent the incorrect inputs.

"""



import requests

api_key = "0d8949a69ced6299cd04906b"

#date
year = input("Enter a year: ")
month = input("Enter a month: ")
day = input("Enter a day: ")

#currency
base_code = input("Enter from currency code:").upper()
rate = input("Enter a rate code: ").upper()

url = f"https://v6.exchangerate-api.com/v6/{api_key}/history/{base_code}/{year}/{month}/{day}"

response = requests.get(url)

if response.ok:
   
   data = response.json()['conversion_rates'][rate]
   print(f" 1 {base_code} was {data} on {day}/{month}/{year}")

else:
   print("API request failed.")