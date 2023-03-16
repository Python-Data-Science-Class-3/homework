## Week 14 Web Scraping Homework
# Question:
# website : 'https://infotechacademy.eu/data_science'
# - From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
# - The scraped data will be cleaned of unwanted characters.
# - The cleaned data will be saved in a json file.
#written by Nuseybe at 16.03.2023


#importing scrapy for making scraping and re for regex
import scrapy
import re


class NewSpider(scrapy.Spider):
    name = "new"
    allowed_domains = ["www.infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
        #taking path for main div class which is including the information about week-title and content
        results = response.xpath("//div[@class='row justify-content-center work-process-with-border']/div/div")  
        #this loop taking information all elements
        for result in results:
            #scraping week number from the website
            week_number = result.xpath(".//div[@class='work-process-image']/span/text()").get()
            #clean the unicode from text
            weeknumber =re.sub(r'[^\x00-\x7F]+','',week_number).strip()
            #scraping content from the website
            detail = result.xpath(".//div[@class='content']/p/text()").get()
            #changing the huge space to a space 
            cont = re.sub(r'["      "]+',' ',detail)
            # claening the new line and cleaning the spaces which are begining and ending of the text
            content = re.sub(r"^\s+|\s+$|\n", "",cont)
            #scraping title from the website
            title = result.xpath(".//div[@class='content']/h3/text()").get()
            #making a yield
            yield{
                "Week Number" : weeknumber,
                "Title" : title,
                "Content" : content
       
            }
        
        