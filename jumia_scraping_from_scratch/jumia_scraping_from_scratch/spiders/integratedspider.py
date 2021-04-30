import scrapy
from scrapy_selenium import SeleniumRequest
import re

class IntegratedspiderSpider(scrapy.Spider):
    name = 'integratedspider'
    def start_requests(self):
        yield SeleniumRequest(
            url = "https://food.jumia.dz/restaurants",
            wait_time = 3,
            screenshot = True,
            callback = self.parse,
            dont_filter = True
        )

    def parse(self, response):
        restaurants = response.xpath('//*[@id="restaurant-list"]/section[2]/div/div/article')
        for restaurant in restaurants:
            name = restaurant.xpath('.//a/section/div[1]/h3/text()').get()
            url = "https://food.jumia.dz"+restaurant.xpath('.//a/@href').get()
            rating = re.findall(r'[0-9\.]+', restaurant.xpath('.//a/section/div[2]/span[1]/text()').get())[0]

            yield {
                    'name':name, 
                    'URL':url, 
                    'RATING':rating
                }

