# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class FormatScrapPipeline(object):
    def process_item(self, item, spider):
        if item['link_noticia']:
            if item['link_noticia'].startswith('//'):
                item['link_noticia'] = item['link_noticia'].replace("//",'')
        if item['titulo_noticia']:
            item['titulo_noticia'] = item['titulo_noticia'].upper()
        return item

class DatabasePipeline(object):
    def open_spider(self, spider):
        self.r = redis.Redis(host='localhost',port=6379)

    def process_item(self, item, spider):
        self.r.incr('indice', amount=1)
        i = self.r.get('indice').decode('utf-8')
        self.r.hmset('indice'+':{}'.format(i),item)
        return item
