import scrapy
import re

class infotech3Spider(scrapy.Spider):
    name = "infotech4"
    # allowed_domains = ["infotechacademy.eu"]
    start_urls = ["https://infotechacademy.eu/data_science"]

    def parse(self, response):
        
        for i in response.css(".work-process-card"):
            weeks = i.css("span.number::text").get().strip()
            headings = i.css('h3::text').get()
            desc = i.css('p::text').get()
            desc_clean = re.sub(r'\s+|\s+$', ' ', desc).strip() 

            yield {
                    "Weeks":weeks,
                    "Headings": headings,
                    "Description": desc_clean
            }

'''
py -3 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activatec 
python -m pip install --upgrade pip 
pip install scrapy 
scrapy startproject infotech3  
cd infotech3 
scrapy genspider infotech4 https://infotechacademy.eu/data_science/
scrapy crawl infotech4     
scrapy crawl infotech4 -o homework.json

'''













        # for i in response.css(".work-process-card"):
        #     week = i.css('span.number::text').get().strip()
        #     title = i.css('h3 ::text').get()
        #     description = i.css('p  ::text').get()
        #     # description = i.css('p  ::text').get()
        #     d1= re.sub((r"^\s+|\s+$", " ", description))
            
        #     # escapes = ''.join([chr(char) for char in range(1, 32)])
        #     # translator = str.maketrans('', '', escapes)
        #     # t = description.translate(translator)
        #     # " ".join(d1.split())

            
            

            # yield{
            #     "Week":week,
            #     "Title" : title,
            #     "Description" : d1
            # }
