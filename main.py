from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys
import argparse

parser = argparse.ArgumentParser(
    description='Retrieve arguments')

parser.add_argument('-t', '--travis', type=bool, help='Tell whether it is running on Travis CI. If you read this, it should be False.', default=False)
args = parser.parse_args()

process = CrawlerProcess(get_project_settings())

process.crawl('gatech', travis=args.travis)
process.start()
