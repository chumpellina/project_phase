from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Cikkcrawler.items import CikkcrawlerItem
from scrapy.selector import Selector


class CikkScraperSpider (CrawlSpider):
    name = "article"
    allowed_domains = ["888.hu"]
    start_urls = ["https://888.hu/search-%C3%B3ra%C3%A1t%C3%A1ll%C3%ADt%C3%A1s"]

    rules = [
        Rule(
            LinkExtractor(
                allow=["oraatall", "idoszamitas", "szenved", "oraval", "idozona"]),
            callback="parse_news",
            follow=False)
    ]

    def parse_news(self, response):
        sel = Selector(response)
        item = CikkcrawlerItem()
        item["source"] = "888.hu"
        item["title"] = sel.xpath("//*[@id='cikkholder']/h1[1]/text()").extract()
        item["lead"] = sel.xpath("//*[@id='cikkholder']/div[3]/span/text()").extract()
        item ["url"] = response.url
        item["date"]= sel.xpath("//*[@id='cikkholder']/p/text()").extract()
        raw_text = sel.xpath("//*[@id='st']/p/text()").extract()
        item["text"] = " ".join(raw_text)
        item["comments"] = "From Facebook API"
        item["likes"] = "From Facebook API"
        item["shares"] = "From Facebook API"

        #yield item

        print (" ".join(raw_text))









