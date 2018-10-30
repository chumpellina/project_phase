from scrapy.spiders import Spider
from wikiSpider.items import Article


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/Python_(programming_language)"]

    def parse (self, response):
        item = Article()
        title = response.xpath("//h1/text()")[0].extract()
        item.name = response.xpath()
        print ("title is: " + title)
        item["title"] = title
        return item


