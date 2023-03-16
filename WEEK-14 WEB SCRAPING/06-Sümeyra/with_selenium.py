""" Question:

website : 'https://infotechacademy.eu/data_science'

From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
The scraped data will be cleaned of unwanted characters.
The cleaned data will be saved in a json file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://infotechacademy.eu/data_science"
driver.get(url)

week_numbers = driver.find_elements(By.CSS_SELECTOR, 'span.number')
week_titles = driver.find_elements(By.CSS_SELECTOR, 'h3')
week_desc = driver.find_elements(By.CSS_SELECTOR, 'p')

weeks = []
for i in range(len(week_numbers)):
    week = {
        'week_number': week_numbers[i].text.strip(),
        'week_title': week_titles[i].text.strip(),
        'description': week_desc[i].text.strip()
    }
    weeks.append(week)

with open('datascience.json', 'w') as f:
    json.dump(weeks, f, indent=4)

driver.quit()
