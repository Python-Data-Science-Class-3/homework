"""Developer  : Tuba Gümüs Esmek
   Date       : 16.10.2023
   Subject    : Web Scraping / Selenium

"""
""" Question:

website : 'https://infotechacademy.eu/data_science'

From the website written above; week numbers, topic names and descriptions will be scraped with the scrapy framework.
The scraped data will be cleaned of unwanted characters.
The cleaned data will be saved in a json file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from warnings import filterwarnings
filterwarnings("ignore")
import time

#Web driver and browser address defined in a variable.
driver = webdriver.Chrome()
driver.get("https://infotechacademy.eu/data_science")

#Calling information in data with class name
numbers = driver.find_elements(By.CLASS_NAME , 'number')
topic_names = driver.find_elements(By.CLASS_NAME , 'content')
#Looping and printing the information in the same class with the for loop
for number in numbers:  
    for content in topic_names:
        data ={f'{number.text} : {content.text} '}
        print(data)
       
#web page auto scroll up and down codes
driver.maximize_window()
driver.execute_script("window.scrollBy(0,2000)","") 
time.sleep(2)
driver.execute_script("window.scrollBy(0,-1900)","") 
time.sleep(4)    
driver.close()

  



      
         

    
