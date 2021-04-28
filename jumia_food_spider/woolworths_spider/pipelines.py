import csv
from scrapy.exporters import CsvItemExporter

class WoolworthsSpiderPipeline(object):

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
