from scrapy import cmdline
cmdline.execute("scrapy crawl craigs -o items.csv -t csv".split())