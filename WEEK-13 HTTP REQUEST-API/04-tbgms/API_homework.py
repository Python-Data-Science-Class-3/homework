'''   Developer : Tuba GÜMÜS ESMEK
      Date      :09.03.2023
      Subject   : HTTP REQUEST-API

      """Question:

NOTICE : YOU DO NOT NEED TO PAY TO THE API SITE. API site provides this service for a fee. But it can also be done with a 2-week PRO trial account.

Write a python script that shows the result by taking the date and currency types from the user to learn from the api site below. You can find the currency symbols on the api site.

api site: https://www.exchangerate-api.com/

For example, when the user wants to learn the USD/TRY exchange rate at 15/01/2023, the result is : "1 USD is 18.7872 TRY on 15/01/2023."

If you want you can use try-except to prevent the incorrect inputs.
'''

import  requests

apiKey  = "284d8db72c310b3118ce2866"

#An input is written to enter the desired information.
currency_code = input("Enter the Currency Code: ").upper()
conversion_code = input("Enter the Conversion Code:  ").upper()
year = input("Enter Year: ")
month = input("Enter Month: ")
day = input("Enter Day: ") 
 
#To get API data, url and API_key are written. Called with get() method.
url = f"https://v6.exchangerate-api.com/v6/284d8db72c310b3118ce2866/history/{currency_code}/{year}/{month}/{day}"

response = requests.get(url)    #Called with get() method.
data = response.json()           #Creating the data() variable and seeing the information with json()
data = response.json()["conversion_rates"][conversion_code]

print(f"1 {currency_code} is {data} on {day}/{month}/{year}")
