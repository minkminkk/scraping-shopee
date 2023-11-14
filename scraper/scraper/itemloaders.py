from itemloaders.processors import Compose, MapCompose, Join, TakeFirst
from scrapy.loader import ItemLoader


# Remove '\r', '\n' from item name and URL
def process_name_url(text_arr):
    return text_arr[0].replace('\r', '').replace('\n', '')


# Compute correct price from scraped value
def process_price(price):
    return price[0] / 100000.000


class ProductLoader(ItemLoader):
    # Specify processor for some fields
    product_name_in = Compose(process_name_url)
    product_price_min_in = Compose(process_price)
    product_price_max_in = Compose(process_price)
    product_url_in = Compose(process_name_url)

    # Other fields
    default_output_processor = TakeFirst()