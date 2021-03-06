# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from products_scraper import items
from products_scraper import db_models, db_settings
from products_scraper import tasks



class ProductsScraperPipeline(object):
    count = 0
    products = []
    prices = []
    def process_item(self, item, spider):
        if type(item) == items.ProductItem:
            self.products.append(dict(item))
            self.count += 1
        else:
            self.prices.append(dict(item))
            self.count += 1
        if self.count >= 1000:
            self.save_items()
            self.count = 0
        return item

    def save_items(self):
        tasks.save_products.delay(self.products)
        tasks.save_prices.delay(self.prices)
        self.products = []
        self.prices = []
