# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B8&fr=search',
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8',
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B82',
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B82&fr=search'
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        sites = hxs.xpath('//li')
        for sel in sites:
            #print sel
            if  sel.xpath('@class').extract() == [' j_thread_list clearfix']:
                #print sel.xpath('@class').extract()
                item = TiebaItem() 
                item['reply'] = sel.xpath('div/div/span/text()').extract()
                item['topic'] = str(sel.xpath('div/div/div/div/a/@title').extract())[3:-2].encode('utf-8')
                item['link'] = 'tieba.baidu.com' + str(sel.xpath('div/div/div/div/a/@href').extract())[3:-2]
                yield item                

        
        newurl = hxs.xpath('//div/div[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href').extract()
        if newurl != []:
            print newurl
            yield self.make_requests_from_url(str(newurl)[3:-2]).replace(callback=self.parse)
            
        '''
        for sel in response.xpath('//li'):
            #print sel 
            if  sel.xpath('@class').extract() == [' j_thread_list clearfix']:
                print sel.xpath('@class').extract()
                item = TiebaItem() 
                item['reply'] = sel.xpath('div/div/span/text()').extract()
                item['topic'] = sel.xpath('div/div/div/div/a/@title').extract()
                item['link'] = 'tieba.baidu.com' + str(sel.xpath('div/div/div/div/a/@href').extract())[3:-2]
                yield item
                
        print response.xpath('//div/div/a[@class="next pagination-item "]/@href').extract()
        for sel in response.xpath('//div/div/a'):   
            #print sel
            if sel.xpath('@class').extract() == ['next pagination-item ']:  
                print sel 
                print sel.xpath('@class').extract()
                nextPage = str(sel.xpath('@href').extract())[3:-2]'''
