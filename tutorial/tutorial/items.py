# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class IccvItem(scrapy.Item):
    #topic = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    code = scrapy.Field()
    project = scrapy.Field()
    poster = scrapy.Field()
    sup_material = scrapy.Field()
    video = scrapy.Field()

class IcmlItem(scrapy.Item):
    #topic = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    
class YoujiItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    
class TiebaItem(scrapy.Item):
    topic = scrapy.Field()
    link = scrapy.Field()
    reply = scrapy.Field()
    
class UserItem(scrapy.Item):
    user = scrapy.Field()
    link = scrapy.Field()
    follower = scrapy.Field()
