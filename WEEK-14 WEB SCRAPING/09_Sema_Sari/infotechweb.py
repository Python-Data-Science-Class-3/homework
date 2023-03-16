import scrapy


class InfotechwebSpider(scrapy.Spider):
    name = "infotechweb"
    #allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
       for course in response.css('div.col-lg-4.col-sm-6'):
       #for course in response.css('div.row justify-content-center work-process-with-border'):
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
        

