from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sor.items import SorItem

class ZirciSorSpider (CrawlSpider):
    name = "zirci"
    allowed_domains = ["zircimanufaktura.hu"]
    start_urls = ["http://www.zircimanufaktura.hu"]

    rules = [
        Rule(
            LinkExtractor(
                allow=["zircimanufaktura.hu"]),
            callback="parse_sor",
            follow=True)
    ]

    def parse_sor(self, response):
        sel = Selector(response)
        item = SorItem()
        names = ["pils", "belga", "buza", "fonix", "apatok-kedvence", "levendulas"]
        item["brewery"] = "Zirci Aátsági Manufaktúra"

        item["beer_name"] = sel.xpath('//*[@id="pils"]/div[1]/div/div/div[2]/div[1]/div/div/div/div/h2/text()').extract()

        item["beer_type"]= sel.xpath('//*[@id="pils"]//p[1]/text()').extract()

        item ["alcohol_vol"] = sel.xpath('//*[@id="pils"]//p[3]/em/strong/text()').extract()

        item["description"] = sel.xpath('//*[@id="pils"]//p[2]/text()').extract()


        yield item










