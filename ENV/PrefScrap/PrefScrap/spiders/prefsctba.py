# -*- coding: utf-8 -*-
import scrapy
from PrefScrap.items import PrefsItem

class PrefsctbaSpider(scrapy.Spider):
    name = 'prefsctba'
    allowed_domains = ['http://www.curitiba.pr.gov.br/']
    start_urls = ['http://www.curitiba.pr.gov.br/']

    def parse(self, response):
        for data in response.xpath("//div[@id='divBoxUltimasNoticias']//li"):
            titulo_noticia = data.xpath("a/text()[last()]").extract_first()
            data_noticia = data.xpath("div[@class='quadro']/text()[1]").extract_first()
            hora_noticia = data.xpath("div[@class='quadro']/text()[2]").extract_first()
            link_noticia = data.xpath("a/@href").extract_first()
            noticia = PrefsItem(titulo_noticia=titulo_noticia,data_noticia=data_noticia,hora_noticia=hora_noticia,link_noticia=link_noticia)
            yield noticia
