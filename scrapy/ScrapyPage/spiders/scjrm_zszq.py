# -*- coding: utf-8 -*-
"""金仁药淘齐_诊所专区"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from scrapy import FormRequest,Request


class scjrm_zszqSpider(scrapy.Spider):
    name = 'scjrm_zszq'
    allowed_domains = ['scjrm']
    start_urls = ['http://www.scjrm.com/zs/index.html']
    # login_url = 'http://www.scjrm.com/site/login.html'

    def __init__(self):
        super().__init__()
        driver = None  # 实例selenium
        cookies = None  # 用来保存cookie

    def parse(self, response):
        # print(response.url)
        # print(response.body.decode('utf-8'))
        for i in range(1, 5):
            time.sleep(1)
            item = CrawlerwebItem()
            name = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[1]/text()' % i).extract()
            cj = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[2]/text()' % i).extract()
            price = response.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[%d]/p[3]/span/text()' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['price'] = price
            yield item



