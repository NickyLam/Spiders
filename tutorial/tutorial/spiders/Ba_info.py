import scrapy
from tutorial.items import BaInfoItem

class BaInfoSpider(scrapy.Spider):
    name = "BaInfo"
    allowed_domains = ["baidu.com"]
    start_urls = (                                  #Dota
        'http://tieba.baidu.com/f/index/forumpark?pcn=%D3%CE%CF%B7&pci=0&ct=1&rn=20&pn=1',                                     #Dota2
    )

    def parse(self, response):
        
        link = {}
        count = 0
        for sel in response.xpath('//div/div/a[@class="ba_href clearfix"]'):
            link[count] = 'tieba.baidu.com' + str(sel.xpath('@href').extract())[3:-2]
            count += 1
        #print link
            
        name = {}
        count = 0
        for sel in response.xpath('//div[@class="ba_content"]/p'):
            if sel.xpath('@class').extract() == [u'ba_name']: 
                
                name[count] = sel.xpath('text()').extract()
                count += 1
        #print name
        
        topic = {}
        follower = {}
        count = 0
        for sel in response.xpath('//div/p[@class="ba_num clearfix"]'):
            topic[count] = sel.xpath('span[@class="ba_p_num"]/text()').extract()
            follower[count] = sel.xpath('span[@class="ba_m_num"]/text()').extract()
            count += 1
        #print topic,follower
          
        '''   
        like = {}
        count = 0
        for sel in response.xpath('//div'):
            print sel 
            print sel.xpath('@class').extract()
            if sel.xpath('@class').extract() == [u"ba_like "]:
                like[count] = sel.xpath('@data-fid').extract()
                count += 1
        print like
        '''
        
        
        for num in range(count):
            item = BaInfoItem()
            item['link'] = link[num]
            item['name'] = name[num]
            item['topic'] = topic[num]
            item['follower'] = follower[num]
            #item['like'] = like[num]
            yield item    
        

        newurl =''
        for sel in response.xpath('//div/div[@class="pagination"]/a'):     
            if sel.xpath('text()').extract() == [u"\u4e0b\u4e00\u9875"]:
                url = sel.xpath('@href').extract()
                if url != []:
                    newurl = 'http://tieba.baidu.com' + str(url)[3:-2]
                    yield self.make_requests_from_url(newurl).replace(callback=self.parse)
                    break
        
        
        
