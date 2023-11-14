# 1. Introduction

This mini project aims to crawl basic data of products in the main categories of [Shopee Vietnam](https://shopee.vn/) using Scrapy, a powerful web sccraping framework in Python. This website are dynamically generated. Website data is pulled from Shopee API (endpoints are tracked via browser's developer tools).

# 2. Technology used

- Python
- Scrapy

# 3. Project Specifications

![Level-1 categories](images/main_categories.png)(Level-1 categories)

- Product data from main (level-1) categories and its children (level-2) categories are extracted into `csv` file.
  - Data from each level-2 category is extracted from a different API endpoint.
- Output `csv` path: `output/{execution_timestamp}.csv`.
- Output fields:
  - `main_cat_name`: Name of level-1 category.
  - `child_cat_name`: Name of level-2 category.
  - `shop_name`: Shop name.
  - `shop_location`: Shop location (city).
  - `product_name`: Name of product.
  - `product_hist_sold`: Quantity of product sold.
  - `product_price_min`: Price of product (minimum).
  - `product_price_max`: Price of product (maximum).
  - `product_rating_avg`: Average rating of product.
  - `product_rating_cnt`: Total amount of ratings.
  - `product_url`: URL of product.

(Note: `product_price` usually has many value depending on product type, therefore is indicated by 2 values `min` and `max`. In case product only has 1 price, the `min` and `max` value should be identical).

- Log files path: `logs/{execution_timestamp}.log`.

# 4. Usage

1. Requirements: Python 3.8+ distribution with `$PATH` already set up.
2. Go to project folder: `cd path/to/scraping-shopee`.
3. Setup Python environment: `make setup`.
   - If you already run `make setup` for an initial time, then just activate the Python virtual environment: `make venv`.
4. Initiate crawling: `make crawl`.
   - Argument:
     - `parse_limit`: Amount of items per level-2 category. If `parse_limit` exceeds 500, only 500 items are crawled per level-2 category due to API limit.
   - Example usage: `make crawl parse_limit=100`.
   - Output path: `scraper/output/{execution_timestamp}.csv`.
   - Log path: `scraper/logs/{execution_timestamp}.log`.