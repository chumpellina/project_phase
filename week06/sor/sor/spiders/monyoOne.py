from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sor.items import SorItem



class SorSpider (CrawlSpider):
    name = "monyoOne"
    allowed_domains = ["monyobrewing.com"]
    start_urls = ['http://monyobrewing.com/soreink/radical-series/', 'http://monyobrewing.com/soreink/collab-series/']

    rules = [
        Rule(
            LinkExtractor(
                allow=[r"monyobrewing.com\/.*-brewing-co\/"]),
                callback="parseOne",
            follow=False),

    ]

    def parseOne(self, response):
        sel = Selector(response)
        item = SorItem()
        item["brewery"] = "Monyo Budapest"

        raw_name = sel.xpath("//h1 [@class='heading__secondary'][1]/text()").extract()
        item["beer_name"] = "".join(raw_name)

        raw_description= sel.xpath("//div [@class='textwidget'][1]/p[2]/text()").extract()
        item["description"] = "".join(raw_description)

        raw_ingredients = sel.xpath("//div [@class='textwidget'][2]/p/text()").extract()
        item["ingredients"] = "".join(raw_ingredients)

        raw_temperature = sel.xpath("//div [@class='textwidget'][3]/p/text()").extract()
        item["temperature"] = "".join(raw_temperature)

        raw_alcohol_vol = sel.xpath("//div [@class='textwidget'][4]/p/text()").extract()
        item["alcohol_vol"] = "".join(raw_alcohol_vol)

        raw_bitterness = sel.xpath("//div [@class='textwidget'][4]/p/text()").extract()
        item["bitterness"] = "".join(raw_bitterness)

        raw_color = sel.xpath("//div [@class='textwidget'][4]/p/text()").extract()
        item["color"] = "".join(raw_color)

        item["price"] = "NaN"

        yield item










