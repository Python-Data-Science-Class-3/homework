import scrapy


class InfotechSpider(scrapy.Spider):
    name = "infotech"
    # allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response): 
        for card in response.css("div.work-process-card"):
            week_number = card.css('span::text').get()
            week_number = week_number.strip()
            topic_name = card.css('div.content h3::text').get()
            topic_name = topic_name.strip()
            description = card.css('div.content p::text').get()
            description = description.strip()
            
            
            yield {
                'Week Number': week_number,
                'Topic Name': topic_name,
                'Description': description,
            }