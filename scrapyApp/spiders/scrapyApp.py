# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

#引入项目
from scrapyApp.items import ScrapyappItem

class itemSpider(scrapy.Spider):
    print('=======开始爬取猫眼电影数据======')

    #这边注意名称需保持一致

    name = "scrapyApp"
    pagelist = [7, 6, 1, 2, 4]

    def start_requests(self):
        for i in self.pagelist:
            self.url = 'http://maoyan.com/board/{page}'.format(page=i)
            yield Request(self.url, callback=self.parse)

    #根据h5标签获取要爬取的内容
    def parse(self, response):
        item = ScrapyappItem()
        selector = Selector(response)
        #navbar 为菜单栏 获取激活的标题 类似['榜单', '最受期待榜']格式 -1为取后面的
        active = selector.xpath('//ul[@class="navbar"]/li/a[@class="active"]/text()').extract()
        #dd元素为top 获取排行榜
        tops = selector.xpath('//dd/i/text()').extract()
        movies = selector.xpath('//div[@class="movie-item-info"]')
        #遍历电影信息
        for i, content in enumerate(movies):
            title = content.xpath('p[@class="name"]/a/text()').extract()
            star = content.xpath('p[2]/text()').extract()
            releasetime = content.xpath('p[3]/text()').extract()
            item['top'] = tops[i] #排行
            item['title'] = title[0]
            #演员 去空格
            item['star'] = star[0].replace(' ', '').replace('\n', '')
            item['type'] = str(active[-1]) #类型
            if releasetime:
                item['releasetime'] = releasetime[0].replace(' ', '').replace('\n', '')
            else:
                item['releasetime'] = ''
            yield item

