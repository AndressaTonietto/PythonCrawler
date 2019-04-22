# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class MycrawlerPipeline(object):
    def process_item(self, item, spider):
        if item['link']:
            if 'futebolatino.lance.com.br' not in item['link']:
                item['link'] = 'http://www.lance.com.br' + item['link']
        return item

class DatabasePipeline(object):
    def open_spider(self, spider):
        self.r = redis.Redis(host='localhost',port=6379)

    def process_item(self, item, spider):
        self.r.incr('indice', amount=1)
        i = self.r.get('indice').decode('utf-8')
        self.r.set('link'+i,item['link'])
        self.r.set('titulo'+i,item['titulo'])
    
