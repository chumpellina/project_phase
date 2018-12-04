from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from sorthree.items import SorthreeItem
import re



class SorSpider (CrawlSpider):
    name = "monyoOne"
    allowed_domains = ["monyobrewing.com"]
    start_urls = ['http://monyobrewing.com/allado-sorok/']

    rules = [
        Rule(
            LinkExtractor(
                allow=[r"monyobrewing.com\/.*-brewing-co\/"]),
                callback="parseOne",
            follow=False),

    ]

    def parseOne(self, response):
        sel = Selector(response)
        item = SorthreeItem()
        item["brewery"] = "Monyo Budapest"

       # nevekOne = ["american beauty", "dead rabbit", "flying rabbit", "funky fritz", "invisible bikini", "schatzi", "summer syndrome", "bipolar bear", "black mamba", "anubis"]

        raw_name = sel.xpath("//h1 [@class='heading__secondary'][1]/text()").extract()
        item["beer_name"] = "".join(raw_name)

        raw_description= sel.xpath("//div [@class='textwidget'][1]/p[2]/text()").extract()
        item["description"] = "".join(raw_description)

        raw_content = sel.xpath("//div[1]/div[1]/text()").extract()
        content = "".join(raw_content)
        infos = content.split(":")
        if len(infos) >=6:
            ingredients_final = infos[1].split(".")[0]
            temp_final = infos [2].split(".")[0]
            alkohol_final = infos[4].split(",")[0]
            bitterness_final = infos[5].split(",")[0]
            color_final = infos[6].split(",")[0]
        else:
            ingredients_final = "NaN"
            temp_final = "NaN"
            alkohol_final = "NaN"
            bitterness_final = "NaN"
            color_final = "NaN"


        item["ingredients"] = "".join(ingredients_final)

        item["temperature"] = "".join(temp_final)

        item["alcohol_vol"] = "".join(alkohol_final)

        item["bitterness"] = "".join(bitterness_final)

        item["color"] = "".join(color_final)

        item["price"] = "NaN"

        yield item










