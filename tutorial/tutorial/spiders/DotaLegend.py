# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = (
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B8&fr=search',
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8',
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B82',
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B82&fr=search',
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%88%80%E5%A1%94%E4%BC%A0%E5%A5%87',
    )

    def parse(self, response):
        for sel in response.xpath('//li[@class="j_thread_list clearfix"]/div'):
            #print sel

            item = TiebaItem() 
            item['reply'] = sel.xpath('div[@class="threadlist_li_left j_threadlist_li_left"]/div[@class="threadlist_rep_num"]/text()').extract()
            item['topic'] = sel.xpath('div/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_text threadlist_title j_th_tit  "]/a/@title').extract()
            item['link'] = 'tieba.baidu.com' + str(sel.xpath('div/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_text threadlist_title j_th_tit  "]/a/@href').extract())[3:-2]
            yield item     
            print item           

        
        newurl = response.xpath('//div/div[@id="frs_list_pager"]/a[@class="next"]/@href').extract()
        print newurl
        if newurl != []:
            newurl = "http://tieba.baidu.com" + str(newurl)[3:-2]
            print newurl
            yield self.make_requests_from_url(newurl).replace(callback=self.parse)            
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
