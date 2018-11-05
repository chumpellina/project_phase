from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from RecursiveScraper.items import RecursivescraperItem
import pandas as pd

class RecursiveScraperSpider (CrawlSpider):
    name = "rs"
    allowed_domains = ["index.hu"]
    start_urls = ["https://www.index.hu"]

    rules = [
        Rule(
            LinkExtractor(
                allow=[".*"]),
             callback = "parse_news",
             follow=True)
    ]

    def parse_news (self, response):
        sel = Selector(response)
        item = RecursivescraperItem()
        item["URL"] = response.request.url
        item["content"] = sel.xpath("div", class_="cikk-torzs").extract()
        return item
