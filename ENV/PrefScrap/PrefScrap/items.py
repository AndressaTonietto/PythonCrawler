# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PrefsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo_noticia = scrapy.Field()
    data_noticia = scrapy.Field()
    hora_noticia = scrapy.Field()
    link_noticia = scrapy.Field()
