# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import pymongo
import time
from scrapy.conf import settings
from scrapy import log

class GatechSamplePipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.stats = db['stats']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg(str(item['url']), level=log.INFO, spider=spider)
        time_elapsed = time.time() - settings['START_TIME']
        self.stats.insert({'elapsed': int(time_elapsed)})

        return item
