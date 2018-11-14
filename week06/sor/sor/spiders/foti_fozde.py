from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sor.items import SorItem
import re


class FotiSorSpider (CrawlSpider):
    name = "foti"
    allowed_domains = ["fotisorfozde.hu"]
    start_urls = ["http://fotisorfozde.hu/products/allando_soreink"]

    rules = [
        Rule(
            LinkExtractor(
                allow=["fotisorfozde.hu/products/allando_soreink"]),
            callback="parse_sor",
            follow=True)
    ]

    def parse_sor(self, response):
        sel = Selector(response)
        item = SorItem()
        item["brewery"] = "Fóti Sörfőzde"

        item["beer_name"] = sel.xpath("//h3/a/text()").extract()

        item["beer_type"]= "NaN"

        item["vol"] = sel.xpath("//div [@class='description']/p/text()[5]").extract()

        item ["alcohol_vol"] = sel.xpath("//div [@class='description']/p/text()[2]").extract()

        item["price"] = sel.xpath("//div [@class='post_content']/text()[3]").extract()

        item["description"] = sel.xpath(("//div [@class='description']/div [@style='text-align:justify;']//p/text()")).extract()


        yield item










