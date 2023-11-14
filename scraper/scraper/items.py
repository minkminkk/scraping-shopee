# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    main_cat_name = scrapy.Field()
    child_cat_name = scrapy.Field()
    shop_name = scrapy.Field()
    shop_location = scrapy.Field()
    product_name = scrapy.Field()
    product_hist_sold = scrapy.Field()
    product_price_min = scrapy.Field()
    product_price_max = scrapy.Field()
    product_rating_avg = scrapy.Field()
    product_rating_cnt = scrapy.Field()
    product_url = scrapy.Field()