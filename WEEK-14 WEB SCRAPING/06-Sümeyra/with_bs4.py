""" Question:

website : 'https://infotechacademy.eu/data_science'

From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
The scraped data will be cleaned of unwanted characters.
The cleaned data will be saved in a json file.
"""

from  bs4 import BeautifulSoup
import requests
import json

url = "https://infotechacademy.eu/data_science"
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

# Find all elements with the 'number' class for week numbers
week_numbers = soup.find_all('span', {'class': 'number'})

# Find all elements with the 'h3' tag for week titles
week_titles = soup.find_all('h3')

#Find all elements with the 'p' tag for week descriptions
week_desc = soup.find_all('p')

# Print the week numbers,titles and descriptions
# for i in range(len(week_numbers)):
#     print(week_numbers[i].text.strip(), '***', week_titles[i].text.strip(),'***',week_desc[i].text.strip())

# Create a dictionary for each week
weeks = []

for i in range(len(week_numbers)):
    week = {
        'week_number': week_numbers[i].text.strip(),
        'week_title': week_titles[i].text.strip(),
        'description':week_desc[i].text.strip()
    }
    weeks.append(week)

# Write the dictionary to a JSON file
with open('datascience.json', 'w') as f:
    json.dump(weeks, f, indent=4)




    
