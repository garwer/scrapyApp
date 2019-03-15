# -*- coding: utf-8 -*-

# Define your item pipelines here
# 将定义
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#将爬取到的数据存取到数据库
import pymysql as mysql
import mysql_model.mysqlUtil as mysqlUtil


class ScrapyappPipeline(object):
    def __init__(self):
        self.conn = mysqlUtil.DB().getCon()
        # self.conn = mysql.connect(host='127.0.0.1',
        #                      port=3306,
        #                      user='root',
        #                      passwd='linjiawei',
        #                      db='actApp',
        #                      charset='utf8')
        #通过cursor执行增删改查
        self.cursor = self.conn.cursor()

        self.cursor.execute("truncate table maoyan_movie")
        #每次初始化前先删掉maoyan_movie【一次5个榜单十个排行50条记录】
        self.conn.commit()
    def process_item(self, item, spider):
        try:
            print(item['star'])
            self.cursor.execute("""insert into maoyan_movie(top, movie_title, movie_star,releasetime,movie_type)
                              values (%s,%s,%s,%s,%s)""",
                                  (item['top'], item['title'], item['star'], item['releasetime'], item['type']))
            self.conn.commit()
        except mysql.Error:
            print("===存储发生错误===")
            print("Error%s,%s,%s,%s" % (item['top'], item['title'], item['star'], item['releasetime']))
        return item

