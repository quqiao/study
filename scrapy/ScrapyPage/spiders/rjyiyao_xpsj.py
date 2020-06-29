# -*- coding: utf-8 -*-
"""嘉事蓉锦医药网_新品上架"""
import scrapy
import time
from ScrapyPage.items import CrawlerwebItem
from selenium import webdriver


class rjyiyaoSpider(scrapy.Spider):
    name = 'rjyiyao_xpsj'
    allowed_domains = ['rjyiyao']
    start_urls = ['http://new.rjyiyao.com/web/product/group/5']

    def __init__(self):
        super().__init__()
        driver = None  # 实例selenium
        cookies = None  # 用来保存cookie

    def parse(self, response):
        for i in range(1, 5):
            time.sleep(3)
            item = CrawlerwebItem()
            name = response.xpath('//*[@id="pageContent"]/div/div[%d]/h1/text()' % i).extract()
            cj = response.xpath('//*[@id="pageContent"]/div/div[%d]/p' % i).extract()
            gg = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[1]/p[1]' % i).extract()
            xq = response.xpath('//*[@id="pageContent"]/div/div[%d]/section[2]/p[1]' % i).extract()
            price = response.xpath('//*[@id="pageContent"]/div/div[%d]/h2/span' % i).extract()
            item['name'] = name
            item['cj'] = cj
            item['gg'] = gg
            item['xq'] = xq
            item['price'] = price
            yield item

