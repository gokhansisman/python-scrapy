# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy2Item(scrapy.Item):
    # define the fields for yo ur item here like:
    _quote = scrapy.Field()
    born = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
