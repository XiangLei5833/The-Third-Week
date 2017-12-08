# -*- coding: utf-8 -*-

import scrapy


class MultipageItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
