from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Cikkcrawler.items import CikkcrawlerItem
from scrapy.selector import Selector


class CikkScraperSpider (CrawlSpider):
    name = "nol"
    allowed_domains = ["nol.hu"]
    start_urls = ["http://nol.hu/kereses?search_txt=%C3%B3ra%C3%A1t%C3%A1ll%C3%ADt%C3%A1s&ujkeres=1"]

    rules = [
        Rule(
            LinkExtractor(
                allow=["orak", "oraatall", "orat", "ido", "almos", "oraval", "idoszamitas" "visszateker", "eloreteker"]),
            callback="parse_news",
            follow=False)
    ]

    def parse_news(self, response):
        sel = Selector(response)
        item = CikkcrawlerItem()
        item["source"] = "nol.hu"
        item["title"] = sel.xpath("//html/body/div[4]/div/div[2]/div/article/h1/text()").extract()
        #/html/body/div[5]/div/div[2]/div/article/h1
        item["lead"] = sel.xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/text()").extract()
        item["url"] = response.url
        item["date"] = sel.xpath("/html/body/div[4]/div/div[2]/div/footer/div[1]/text()").extract()
        item["text"] = sel.xpath("/html/body/div[4]/div/div[2]/div/article/div[4]/p/text()").extract()
        item["comments"] = sel.xpath("//*[@id='comments_1607199']/div[2]/text()").extract()
        item["likes"] = "From Facebook API"
        item["shares"] = "From Facebook API"

        yield item

