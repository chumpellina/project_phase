# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CikkcrawlerItem(scrapy.Item):

    url = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    lead = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    comments = scrapy.Field()
    likes = scrapy.Field()
    shares = scrapy.Field()

