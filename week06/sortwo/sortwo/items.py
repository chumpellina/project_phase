# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SortwoItem(scrapy.Item):
    brewery = scrapy.Field()
    beer_name = scrapy.Field()
    beer_type = scrapy.Field()
    alcohol_vol = scrapy.Field()
    vol = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    ingredients = scrapy.Field()
    bitterness = scrapy.Field()
    temperature = scrapy.Field()
    color = scrapy.Field()
    url = scrapy.Field()
