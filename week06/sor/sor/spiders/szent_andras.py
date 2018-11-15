from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sor.items import SorItem
import re


class FotiSorSpider (CrawlSpider):
    name = "szent_andras"
    allowed_domains = ["szentandrassorfozde.hu"]
    start_urls = ["https://szentandrassorfozde.hu/hu/termekeink?ao_confirm"]

    rules = [
        Rule(
            LinkExtractor(
                allow=["szentandrassorfozde.hu/hu/tartalom/sorfajtak/"]),
            callback="parse_sor",
            follow=True)
    ]

    def parse_sor(self, response):
        sel = Selector(response)
        item = SorItem()
        item["brewery"] = "Szent András Sörfőzde"

        raw_name = sel.xpath("//*[@class='portfolio-content']//h2/text()").extract()
        item["beer_name"] = "".join(raw_name)

        raw_type = (sel.xpath("//div/div[2]/div/div[2]/div/div/text()").extract())
        item["beer_type"]= "".join(raw_type)

        item["vol"] = "NaN"

        item ["alcohol_vol"] = "NaN"

        item["price"] = "NaN"

        raw_description = sel.xpath("//div[@class='portfolio-content']//p/text()").extract()
        item["description"] = "".join(raw_description)


        yield item












