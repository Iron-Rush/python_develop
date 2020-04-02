# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    # 启动的url链接
    start_urls = ['http://python123.io/ws/demo.html']

    #   完整版代码
    # def start_requests(self):
    #     urls = [
    #         'http://python123.io/ws/demo.html'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 对返回页面进行解析和操作
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)
        # pass