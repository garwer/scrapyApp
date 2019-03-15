# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#要爬取的数据 【排行、电影名、演员、上映时间、评分】
class ScrapyappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    top = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    releasetime = scrapy.Field()
    type = scrapy.Field()
    pass
