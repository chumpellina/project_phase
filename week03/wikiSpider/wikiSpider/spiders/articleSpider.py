from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article
from scrapy.cmdline import execute

class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/Python_(programming_language)"]

    def parse (self, response):
        item = Article()
        title = response.xpath("//h1/text()")[0].extract()
        print ("title is: " + title)
        item["title"] = title
        return item



execute("scrapy crawl article")