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
                allow=[".*"]),
            callback="parse_news",
            follow=False)
    ]


    def parse_news(self, response):
        sel = Selector(response)
        item = CikkcrawlerItem()
        item["title"] = sel.xpath('//*[@id="content"]/div[@class = "main-content"]/div/div/div/div/a/h2/text()', id_="content").extract()
        item["lead"] = sel.xpath('//*[@id="content"]/div[@class ="main-content"]/div/div/div/div/p/text()', id_="content").extract()
        #item ["urls"] = sel.xpath("//*[@id='content']/div/div/div/div/div/a/text()").extract()
        #print (sel.xpath("//*[@id='content']/div/div/div/div/div/a/text()").extract())




