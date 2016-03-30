#!/usr/bin/python
#-*-coding: utf-8 -*-

import scrapy

from tutorial.items import YoujiItem

class YoujiSpider(scrapy.Spider):
    name = 'youji'
    allowed_domains = ['baidu.com']
    start_urls = ['http://lvyou.baidu.com/user/reply/715fcb6399c14e53f5562721']
    
    
    def parse(self, response):
        # for sel in response.xpath('//tr'):
        #     item = YoujiItem()
        #     item['title'] = sel.xpath('td[2]/a/text()').extract()
        #     link = sel.xpath('td[2]/a/@href').extract()
        #     item['link'] = 'http://lvyou.baidu.com' + str(link)[3:-2]
        #     yield item
        
        middle = ''
        for sel in response.xpath('//ul/li'):
            clas = sel.xpath('@class').extract()
            if clas == ["nav-reply"]:
                middle = str(sel.xpath('a/@href').extract())[3:-2] 
        
        for sel in response.xpath('//div/span/a'):
            if sel.xpath('@class').extract() == ['pagelist-top BP_trigger']:
                yield 'http://lvyou.baidu.com' + middle + str(sel.xpath('@href').extract())[3:-2] 

            
        # for sel in response.xpath('//div/span'):
        #     back = sel.xpath('a[class = "pagelist-top BP_trigger"]/text()').extract()
        #     page = front + '?' + str(back)[3:-2]
        #     nextPage.append(page)
        # print nextPage
        
        
            
           