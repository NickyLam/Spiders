# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = (
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B8&fr=search',    #梦幻西游
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B82&fr=search',   #梦幻西游2
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8',               #大话西游    
#        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B82',              #大话西游2
#        'http://tieba.baidu.com/f?ie=utf-8&kw=lol',                                               #LOL
#        'http://tieba.baidu.com/f?ie=utf-8&kw=Dota&fr=search',                                     #Dota
        'http://tieba.baidu.com/f?ie=utf-8&kw=dota2',                                             #Dota2  
    )

    def parse(self, response):
        for sel in response.xpath('//li[@class=" j_thread_list clearfix"]/div'):
            print sel
            #print sel.xpath('@class').extract()
            item = TiebaItem() 
            item['reply'] = sel.xpath('div/span[@class="threadlist_rep_num center_text"]/text()').extract()
            item['topic'] = sel.xpath('div/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            item['link'] = 'tieba.baidu.com' + str(sel.xpath('div/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract())[3:-2]
            yield item                

        
        newurl = response.xpath('//div/div[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href').extract()
        if newurl != []:
            print newurl
            yield self.make_requests_from_url(str(newurl)[3:-2]).replace(callback=self.parse)
