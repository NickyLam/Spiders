import scrapy 
from tutorial.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = 'baidu.com'
    start_urls = [
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B8&fr=search',
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E8%AF%9D%E8%A5%BF%E6%B8%B8&fr=search'
    ]
    
def parse(self, response):
    for sel in response.xpath('//li[contains(@class,"j_thread_list thread_top j_thread_list clearfix")]'):
        item = TiebaItem()
        item['reply'] = sel.xpath('div/span[contains(@class,"threadlist_rep_num center_text")]/text()').extract()
        item['title'] = sel.xpath('div/div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/@title').extract()
        item['link'] = 'tieba.baidu.com' + str(sel.xpath('div/div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/@href').extract())[3:-2]
        yield item