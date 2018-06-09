# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

DATA_FILE_PATH = "data/51ape.txt"

# 爬虫爬到的数据以JSON格式保存到51ape.txt
class Crawl51ApePipeline(object):
    def __init__(self):
        self.file = open(DATA_FILE_PATH, 'a')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False).encode("utf-8"))
        self.file.write("\n")
        return item