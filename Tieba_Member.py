import scrapy
from tutorial.items import MemberItem

class TiebaMemberfoSpider(scrapy.Spider):
    name = "TiebaMember"
    allowed_domains = ["baidu.com"]
    start_urls = (                                  #Dota
        'http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%C3%CE%BB%C3%CE%F7%D3%CE',                                     
    )

    def parse(self, response):
        
        for sel in response.xpath('//div[@class="name_wrap"]'):
            item = MemberItem()
            item['name'] = sel.xpath('a/text()').extract()
            item['link'] = 'http://tieba.baidu.com' + str(sel.xpath('a/@href').extract())[3:-2]
            yield item
            
        for sel in response.xpath('//li/a'):
            if sel.xpath('@class').extract() == ["next_page"]:
                nextpage = 'http://tieba.baidu.com' + str(sel.xpath('@href').extract())[3:-2]
                yield self.make_requests_from_url(nextpage).replace(callback=self.parse) 
        