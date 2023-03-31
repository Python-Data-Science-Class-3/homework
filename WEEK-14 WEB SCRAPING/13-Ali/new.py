import scrapy
import re


class NewSpider(scrapy.Spider):
    name = "new"
    # allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
        for part in response.css('div.col-lg-4.col-sm-6'):
        
            week = part.css('div.work-process-image span ::text').get()
            topic = part.css('h3::text').get()
            description = part.css('p::text').get()


            def while_newLine(string2):                      #with these two functions spaces and new limes \n are removed 
                while '\n' in string2:
                    string2 = string2.replace('\n', '')
                return string2
            

            def while_multiSpace(string1):
                while '  ' in string1:
                    string1 = string1.replace('  ', ' ')
                return string1

            week = while_multiSpace(week)
            week = while_newLine(week)
            week = week.strip()
            topic = topic.strip()
            description = while_multiSpace(description)
            description = while_newLine(description)
            description = description.strip()

            yield {
                'week': week,
                'topic': topic,
                'description': description,
            }
