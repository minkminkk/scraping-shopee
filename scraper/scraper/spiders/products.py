import scrapy
from datetime import datetime
from scraper.items import Product
from scraper.category_cls import get_category_tree
from scraper.itemloaders import ProductLoader


class ProductsSpider(scrapy.Spider):
    """Spider for crawling product info in main categories
    
    Command line argument:
    - parse_limit: Maximum number of items parsed per level-2 category.
    Defaults to 50.
    (If parse_limit > 500, only 500 items are scraped per category due to
    limitations in Shopee API).

    Usage: scrapy crawl products [-a parse_limit=50]
    """
    name = "products"
    allowed_domains = ["shopee.vn"]


    def start_requests(self):
        """Get category tree from Shopee API and send requests to 
        fetch level-2 category info
        """
        # Command line argument parse_limit validation (-a input is string type)
        self.parse_limit = getattr(self, 'parse_limit', '500')
        if not self.parse_limit.isnumeric():
            raise TypeError('parse_limit must be an integer')
        
        # Send request to 2nd-level category and scrape product data from API
        cat_tree = get_category_tree()
        for main_cat in cat_tree.children[:2]:
            for child_cat in main_cat.children:
                # Specify URL and send request
                url = 'https://shopee.vn/api/v4/recommend/recommend?bundle=' \
                    + f'category_landing_page&cat_level={child_cat.level}' \
                    + f'&catid={child_cat.id}&limit={self.parse_limit}&offset=0'
                yield scrapy.Request(
                    url = url,
                    callback = self.parse_item,
                    meta = {
                        'main_cat_name': main_cat.name, 
                        'child_cat_name': child_cat.name
                    }
                )


    def parse_item(self, response):
        """Parse item info and write into output.csv
        """
        # Response as dict
        response_json = response.json()

        # Get product info
        product_list = response_json['data']['sections'][0]['data']['item']
        for product in product_list:
            loader = ProductLoader(item = Product(), response = response)

            # Add values to items
            loader.add_value('main_cat_name', response.meta['main_cat_name'])
            loader.add_value('child_cat_name', response.meta['child_cat_name'])
            loader.add_value('shop_name', product['shop_name'])
            loader.add_value('shop_location', product['shop_location'])
            loader.add_value('product_name', product['name'])
            loader.add_value(
                'product_url', 
                f"https://shopee.vn/{product['name'].replace(' ', '-')}" \
                    + f"-i.{product['shopid']}.{product['itemid']}"
            )
            loader.add_value('product_hist_sold', product['historical_sold'])
            loader.add_value('product_price_min', product['price_min'])
            loader.add_value('product_price_max', product['price_max'])
            loader.add_value(
                'product_rating_avg', product['item_rating']['rating_star']
            )
            loader.add_value(
                'product_rating_cnt', product['item_rating']['rating_count']
            )

            yield loader.load_item()