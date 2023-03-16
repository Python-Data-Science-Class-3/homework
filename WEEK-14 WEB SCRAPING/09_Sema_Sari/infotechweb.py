""" Question:

website : 'https://infotechacademy.eu/data_science'

From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
The scraped data will be cleaned of unwanted characters.
The cleaned data will be saved in a json file.
"""







import scrapy


class InfotechwebSpider(scrapy.Spider):
    name = "infotechweb"
    #allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
       for course in response.css('div.col-lg-4.col-sm-6'):

            week = course.css('div.work-process-image span ::text').get()
            topic = course.css('h3::text').get()
            description = course.css('p::text').get()

            week=week.strip()
            topic = topic.strip()
            description = description.strip()

            yield {
                'week': week,
                'topic': topic,
                'description': description
            }
        

