import scrapy
import re


class Deneme2Spider(scrapy.Spider):
    name = "deneme2"
    # allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
        for i in response.css(".work-process-card"):
            week = i.css("span.number::text").get().strip()
            heading = i.css('h3::text').get()
            text = i.css('p::text').get()
            text1 = re.sub(r'\s+', ' ', text).strip() 

            yield {
                    "Week":week,
                    "Topic": heading,
                    "Description": text1
            }