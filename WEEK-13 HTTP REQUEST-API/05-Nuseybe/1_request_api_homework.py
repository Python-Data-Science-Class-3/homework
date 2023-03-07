import requests
money_code = input("Please input a money code :  ")
rate = input("Please input the money currency rate code :  ")
date = input("Please input the date  (like day/month/year) :  ").split("/")

url = f"https://v6.exchangerate-api.com/v6/b7af4957b142f323a4b710df/history/{money_code}/{date[2]}/{date[1]}/{date[0]}"
try: 
    response = requests.get (url)
    result = response.json()["conversion_rates"][rate]
    print(f"The result is : 1 {money_code} is {result} on {date[0]}/{date[1]}/{date[2]}   ")
except:
    print(f" There is no information about {rate} on {date[0]}/{date[1]}/{date[2]}.")