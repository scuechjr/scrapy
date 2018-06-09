# -*- coding: utf-8 -*-

import scrapy
import json
from crawl51ape.items import Crawl51ApeItem

class Crawl51apeSpider(scrapy.Spider):
    name = "51ape"
    allowed_domains = ["51ape.com"]
    start_urls = [
        "http://www.51ape.com/%E7%BB%8F%E5%85%B8%E6%AD%8C%E6%9B%B2/"
    ]

    def parse(self, response):
    	sel = scrapy.Selector(response)
    	for itemUrl in response.xpath('/html/body/div[1]/div/div[6]/div[2]/div[1]/ul/li/a/@href').extract():
    		yield scrapy.Request(url=itemUrl, callback=self.parse_item)

        for listUrl in response.xpath('//div[@class="mt_1 listpage b_t_d b_b_d lh50"]/a[@href]/@href').extract():
            listUrl = "http://www.51ape.com/" + listUrl
            print "################" + listUrl
            yield scrapy.Request(url=listUrl, callback=self.parse)

    def parse_item(self, response):
        item = Crawl51ApeItem()

        item["name"] = response.xpath('/html/body/div[1]/div/div[6]/h1/text()')[0].extract()  # 歌曲名
        item["names"] = response.xpath('/html/body/div[1]/div/div[6]/ul/li[5]/text()')[0].extract()
        item["area"] = response.xpath('//div[@class="fl over w638"]/ul/li[3]/a/text()')[0].extract()  # 所属分类
        if item["area"] == "":
            item["area"] = response.xpath('//div[@class="fl over w638"]/ul/li[3]/a/@title')[0].extract()  # 所属分类
        item["form"] = response.xpath('/html/body/div[1]/div/div[6]/h3[1]/text()')[0].extract()  # 选自 来源
        item["types"] = response.xpath('/html/body/div[1]/div/div[6]/h3[2]/text()')[0].extract()  # 音质类型
        item["length"] = response.xpath('/html/body/div[1]/div/div[6]/h3[3]/text()')[0].extract()  # 文件的大小
        item["language"] = response.xpath('/html/body/div[1]/div/div[6]/h3[4]/text()')[0].extract()  # 语言
        item["data_time"] = response.xpath('/html/body/div[1]/div/div[6]/h3[5]/text()')[0].extract()  # 更新时间
        item["baidu_url"] = response.xpath('/html/body/div[1]/div/div[6]/a/@href')[0].extract()  # 网盘链接
        item["baidu_se"] = response.xpath('/html/body/div[1]/div/div[6]/b/text()')[1].extract().encode('utf-8').replace("密码：", "").replace("无", "")  # 网盘提取密码
        item["words"] = response.xpath('//*[@id="newstext_2"]/h3[1]/a/text()')[0].extract()  #
        item["music"] = response.xpath('//*[@id="newstext_2"]/h3[2]/a/text()')[0].extract()
        item["music_info"] = "\n".join(response.xpath('//*[@id="newstext_2"]/p/text()').extract())
        item["url"] = response.url


        # print json.dumps(dict(item), ensure_ascii=False).encode("utf-8")

        return item
