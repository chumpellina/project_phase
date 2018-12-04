
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sortwo.items import SortwoItem
import re


class ZirciSorSpider (CrawlSpider):
    name = "zirci"
    allowed_domains = ["zircimanufaktura.hu"]
    start_urls = ["http://zircimanufaktura.hu"]

    rules = [
        Rule(
            LinkExtractor(
                allow=[r"zircimanufaktura\.hu\#home$"]),
            callback="parse_sor",
            follow=False)
    ]

    def parse_sor(self, response):
        sel = Selector(response)
        item = SortwoItem()
        item["brewery"] = "Zirci Manufaktúra"

        item["url"] = response.request.url

        raw_name = sel.xpath("//h2/text()").extract()
        item["beer_name"] = raw_name[1:]

        raw_type = sel.xpath("//div/p[1]/strong/text()").extract()
        rawer_type = raw_type[1:-1]

        item["beer_type"]= rawer_type


        raw_des = sel.xpath("//p[2]/text()").extract()

        item["description"] = ''.join(raw_des [1:-2])

        item["alcohol_vol"] = sel.xpath("//em/strong/span/text()").extract()

        print (item["beer_type"])
       # yield item
