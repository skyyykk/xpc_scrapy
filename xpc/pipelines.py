# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy_redis

class XpcPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user='root',
            password = '123456',
            db = 'xpc',
            charset = 'utf8mb4'
        )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        if not hasattr(item, 'table_name'):
            return item
        cols,values = zip(*item.items())
        sql = 'INSERT INTO %s (%s) VALUES (%s);'% (item.table_name,','.join(cols),','.join(['%s']*len(values)))
        # on duplicate key update
        # print(sql)
        self.cur.execute(sql,values)
        self.conn.commit()
        return item


    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()








