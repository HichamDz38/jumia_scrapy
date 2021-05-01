import scrapy
import re
from scrapy_selenium import SeleniumRequest
from jumia_scraping_from_scratch.items import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class IntegratedspiderSpider(scrapy.Spider):
    name = 'integratedspider'
    rotate_user_agent = True
    def start_requests(self):
        yield SeleniumRequest(
            url = "https://food.jumia.dz/restaurants",
            wait_time = 300,
            screenshot = True,
            callback = self.parse,
            dont_filter = True,
            wait_until=EC.presence_of_element_located((By.XPATH, '//*[@id="restaurant-list"]/section[2]/div[1]/div/div/article[1]/a'))
        )

    def parse(self, response):
        with open('image.png', 'wb') as image_file:
            image_file.write(response.meta['screenshot'])
        restaurants = response.xpath('//*[@id="restaurant-list"]/section[2]/div/div/article')
        for restaurant in restaurants:
            name = ''
            url = ''
            rating = ''
            price = ''
            cuisine =''
            try:
                name = restaurant.xpath('.//a/section/div[1]/h3/text()').get()
                url = "https://food.jumia.dz"+restaurant.xpath('.//a/@href').get()
                rating = re.findall(r'[0-9\.]+', restaurant.xpath('.//a/section/div[2]/span[1]/text()').get())[0]
                elements = list(map(lambda x:x.strip(),restaurant.xpath('.//a/section/div[2]/span[2]/text()').get().split('•')))
                price = elements[0]
                cuisine = ' '.join(elements[1:])

            except Exception as e:
                print("extracting values error ",e)

            try:
                
                item = JumiaScrapingFromScratchItem()

                item['name'] = name
                item['url'] = url
                item['rating'] = rating
                item['price'] = price
                item["cuisine"] = cuisine
                # print({'NAME': name, 'URL': url, 'RATING': rating,'PRICE' : price,"CUISINE" : cuisine})
                
                
                # yield {'NAME': name, 'URL': url, 'RATING': rating,'PRICE' : price,"CUISINE" : cuisine}
                yield item

            except Exception as e:
                print('packaging error ',e)
