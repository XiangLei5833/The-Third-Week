# -*- coding: utf-8 -*-

import scrapy


class GithubItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
