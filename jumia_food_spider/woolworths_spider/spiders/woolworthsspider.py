"""
# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem

class WoolworthsspiderSpider(scrapy.Spider):
    name = 'woolworthsspider'
    allowed_domains = ['woolworths.com.au']
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def parse(self, response):
    	for Item in responce.xpath('')
        item = PropertiesItem()



//*[@id="center-panel"]/div/wow-tile-list-with-content/ng-transclude/wow-browse-tile-list/wow-tile-list/div/div[1]/div[3]/wow-tile[1]/div/wow-shelf-product-tile/div/div[1]/div/h3/a
//*[@id="center-panel"]/div/wow-tile-list-with-content/ng-transclude/wow-browse-tile-list/wow-tile-list/div/div[1]/div[3]/wow-tile[9]/div/wow-shelf-product-tile/div/div[1]/div/h3/a

"""

# -*- coding: utf-8 -*-
import scrapy
from woolworths_spider.items import *
from scrapy import Selector
import re


class WoolworthsspiderSpider(scrapy.Spider):
    name = 'woolworthsspider'
    pattern = re.compile('[0-9.]+')
    base_url = 'https://www.woolworths.com.au'
    allowed_domains = ['www.woolworths.com.au']
    enable_crawl = ["https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"]

    def start_requests(self):
        for url in self.enable_crawl:
            yield scrapy.Request(url=url,callback=self.parse_product)


    def parse_product(self, response):
        sel = Selector(response)
        breadcrumb=[]
        for i in range(1,4):
            bread=sel.xpath('//*[@id="center-panel"]/div/wow-tile-list-with-content/ng-transclude/wow-browse-tile-list/wow-tile-list/div/div[1]/div[1]/wow-breadcrumbs/div/ul/li['+str(i)+']/span/a/text()').extract()
            breadcrumb.append(bread[0])
        bread=sel.xpath('//*[@id="center-panel"]/div/wow-tile-list-with-content/ng-transclude/wow-browse-tile-list/wow-tile-list/div/div[1]/div[1]/wow-breadcrumbs/div/ul/li[4]/span/span/text()').extract()
        breadcrumb.append(bread[0])
        divs = sel.css('.shelfProductTile-descriptionLink::text').extract()
        for div in divs:
            item = woolworthsItem()
            item['name'] = div.strip()
            item['breadcrumb']=breadcrumb
            yield item

        divs = sel.css('.shelfBundleTile-title::text').extract()
        for div in divs:
            item = woolworthsItem()
            item['name'] = div.strip()
            item['breadcrumb']=breadcrumb
            yield item
        