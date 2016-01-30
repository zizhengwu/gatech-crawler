# Scrapy settings for gatech project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'gatech'

SPIDER_MODULES = ['gatech.spiders']
NEWSPIDER_MODULE = 'gatech.spiders'
ITEM_PIPELINES = {'gatech.pipelines.GatechSamplePipeline': 1000}
LOG_LEVEL = 'INFO'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gatech (+http://www.yourdomain.com)'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "gatech"
MONGODB_COLLECTION = "pages"