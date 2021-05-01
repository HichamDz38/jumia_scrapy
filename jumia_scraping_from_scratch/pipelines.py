# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class JumiaScrapingFromScratchPipeline:

    def __init__(self):
        self.f = open("result.csv", 'wb')
        self.exp = CsvItemExporter(self.f)
        self.exp.start_exporting()

    def close_spider(self, spider):
        self.exp.finish_exporting()
        self.f.close()

    def process_item(self, item, spider):
        self.exp.export_item(item)
        return item