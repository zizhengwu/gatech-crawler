from scrapy import cmdline
cmdline.execute("scrapy crawl gatech -o items.csv -t csv".split())