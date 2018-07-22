# -*- coding: utf-8 -*-
import scrapy


class SampleSpider(scrapy.Spider):
    name = 'sample'
    allowed_domains = ['sample.com']
    start_urls = ['http://sample.com/']

    def parse(self, response):
        pass
