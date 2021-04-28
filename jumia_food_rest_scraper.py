import scrapy

class BlogSpider(scrapy.Spider):
    name = 'restaurant_spider'
    start_urls = ['https://food.jumia.dz/restaurants']

    def parse(self, response):
        for article in response.css('article'):
            yield {'title': article.css('::a').get()}