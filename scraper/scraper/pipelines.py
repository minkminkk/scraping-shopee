# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import datetime


class ProductPipeline:
    def open_spider(self, spider):
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        self.file = open(f'output/{timestamp}.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)

        # Define field order at output file
        self.exporter.fields_to_export = [
            'main_cat_name',
            'child_cat_name',
            'shop_name',
            'shop_location',
            'product_name',
            'product_hist_sold',
            'product_price_min',
            'product_price_max',
            'product_rating_avg',
            'product_rating_cnt',
            'product_url'
        ]
        
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.exporter.export_item(item)
        return item
            
