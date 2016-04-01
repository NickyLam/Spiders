#!/usr/bin/python
#-*-coding: utf-8 -*-

import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import UserItem

class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['baidu.com']
    start_urls = {
        'http://lvyou.baidu.com/user/follow/715fcb6399c14e53f5562721'
    }
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="follow-block"]'):
            item = UserItem()
            item['user'] = sel.xpath('div[@class="follow-detail"]/a/text()').extract()
            item['link'] = 'http://lvyou.baidu.com/' + str(sel.xpath('div[@class="follow-detail"]/a/@href').extract())[3:-2]
            follow_info = sel.xpath('div[@class="follow-detail"]/div[@class="follow-info"]/text()').extract()
            item['follower'] = follow_info
            yield item
            
            followe_link = item['link'].split('/user')
            followe_link = followe_link[0] + '/user/follow' + followe_link[1]
            if item['link'] != []:
                yield self.make_requests_from_url(followe_link).replace(callback=self.parse)
        
        