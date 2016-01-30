from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from gatech.items import GatechItem
import html2text

class MySpider(CrawlSpider):
    name = "gatech"
    allowed_domains = ["gatech.edu"]
    start_urls = ["http://www.gatech.edu/"]

    rules = (
        Rule(SgmlLinkExtractor(), callback="parse_items", follow= False),
    )

    def parse_items(self, response):
        html2text.BODY_WIDTH = 0
        item = GatechItem()
        converter = html2text.HTML2Text()

        item['url'] = response.url
        item['text'] = converter.handle((response.body.decode(response.encoding)).encode('utf-8').decode('utf-8')).replace('\n', '')

        return item
