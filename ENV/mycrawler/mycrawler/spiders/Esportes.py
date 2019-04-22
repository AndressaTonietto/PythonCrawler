# -*- coding: utf-8 -*-
import scrapy
from mycrawler.items import MycrawlerItem as mcrawler

class EsportesSpider(scrapy.Spider):
    name = 'Esportes'
    allowed_domains = ['www.lance.com.br']
    start_urls = ['http://www.lance.com.br/']

    def parse(self, response):
        for data in response.xpath("//div[@class='listing-title']//*"):
            link = data.xpath("@href").extract_first()
            titulo = data.xpath("normalize-space(text())").extract_first()

            noticia = mcrawler(link=link,titulo=titulo)
            yield noticia
    #pass
