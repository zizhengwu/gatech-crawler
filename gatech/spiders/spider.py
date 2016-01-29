from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from gatech.items import GatechItem
import lxml.html

class MySpider(CrawlSpider):
    name = "gatech"
    allowed_domains = ["gatech.edu"]
    start_urls = ["http://www.gatech.edu/"]

    rules = (
        Rule(SgmlLinkExtractor(), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        root = lxml.html.fromstring(response.body)
        lxml.etree.strip_elements(root, lxml.etree.Comment, "script", "head")

        item = GatechItem()
        item['url'] = response.url
        item['text'] = lxml.html.tostring(root, method="text", encoding=unicode)
        return item
