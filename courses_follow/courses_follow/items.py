# -*- coding: utf-8 -*-

import scrapy


class CoursesImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
