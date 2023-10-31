# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SupermarketItem(scrapy.Item):
    nome = scrapy.Field()
    preco_original = scrapy.Field()
    preco_oferta = scrapy.Field()
    img_pequena = scrapy.Field()
    img_grande = scrapy.Field()
    departamento = scrapy.Field()
    mercado = scrapy.Field()
    url = scrapy.Field()
    data = scrapy.Field()
