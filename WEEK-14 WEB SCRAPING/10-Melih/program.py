""" 

Developer : Melih Orhan Yilmaz
Date      : 16.03.2023

Application : Web Scraping

Explanation : 

    website : 'https://infotechacademy.eu/data_science'

    From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
    The scraped data will be cleaned of unwanted characters.
    The cleaned data will be saved in a json file.


"""


import scrapy
import re


class ProgramSpider(scrapy.Spider):
    name = "program"
    start_urls = ["https://infotechacademy.eu/data_science"]

    # Default entry point for Scrapy to start the crawling process
    def parse(self, response):
        # Path for main div class with week, title and content information
        for info in response.xpath("//div[@class='work-process-card']"):
            # Scraping week number from the website
            week_number = info.xpath('.//span[@class="number"]/text()').get()
            # Scraping name from the website
            topic_name = info.xpath('.//div[@class="content"]/h3/text()').get()
            # Scraping description from the website
            description = info.xpath('.//div[@class="content"]/p/text()').get()

            yield{
                    # cleaned of unwanted characters
                    "Week Number" : week_number.strip(),
                    "Topic Name" : topic_name,
                    # '\s+' matches all whitespace characters inside the element and replaces them with a single space character ' '
                    "Description" : re.sub('\s+', ' ', description.strip())
                }

"""
py -3.7 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
python -m pip install --upgrade pip
pip install scrapy
scrapy startproject program
cd program
scrapy genspider program https://infotechacademy.eu/data_science
scrapy crawl program
scrapy crawl program -o info.json
"""