# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from baidu_wangpan_parse import BaiduWangpan

DATA_FILE_PATH = "../data/51ape_url.txt"

# 爬虫爬到的数据，通过BaiduWangpan解析实际下载地址，解析URL保存到51ape_url.txt
class Crawl51ApePipeline(object):
    def __init__(self):
        self.file = open(DATA_FILE_PATH, 'a')

    def process_item(self, item, spider):
        # python baidu_wangpan_parse.py -f false -e false -l http://pan.baidu.com/s/1hrFJVus
        if item["baidu_se"] is None:
            baiduWangpan = BaiduWangpan(isEncrypt=False,
                                    isFolder=False,
                                    link=item["baidu_url"],
                                    password=item["baidu_se"])
        else:
            baiduWangpan = BaiduWangpan(isEncrypt=True,
                                    isFolder=False,
                                    link=item["baidu_url"],
                                    password=item["baidu_se"])
        result = baiduWangpan.getDownloadURL();
        if result is not None:
            self.file.write(result["list"][0]['dlink'])
            self.file.write("\n")
            print result["list"][0]['dlink']
        return item