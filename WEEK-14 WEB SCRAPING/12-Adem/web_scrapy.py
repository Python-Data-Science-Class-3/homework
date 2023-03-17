"""
website : 'https://infotechacademy.eu/data_science'

From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
The scraped data will be cleaned of unwanted characters.
The cleaned data will be saved in a json file.
"""

import scrapy
import re
import json

class DataScienceSpider(scrapy.Spider):
    name = "data_science"

    start_urls = [
        "https://infotechacademy.eu/data_science",
    ]

    def parse(self, response):
        data = []
        # Get the week numbers, week_title, and week_description 
        for week in response.xpath('//div[@class="work-process-card"]'):
           
            week_number = week.css("span::text").get().strip()
            week_title = week.css("h3::text").get().strip()
            week_description = week.css("p::text").get().strip()
           
           # Clean the data by removing unwanted characters
            week_number = re.sub(r'[^\w\s]', "", week_number).strip()
            week_title = re.sub(r'[^\w\s]', "", week_title).strip()
            week_description = " ".join(week_description.split())

            # Add the data to the list           
            data.append({'week_number': week_number, 'week_title': week_title, 'description': week_description})

        # Save the data in a JSON file
        with open('infotech_data.json', 'w') as f:
            json.dump(data, f)
