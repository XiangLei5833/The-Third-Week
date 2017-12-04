#!/usr/bin/env python3

import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    """ 所有 scrapy 爬虫需要写一个 Spider 类，这个类继承 scrapy.Spider 类。在这个类中定义要请求的网站和链接，以及如何从网页中返回数据等"""

    name = 'shiyanlou-courses'    # 爬虫标识符号，在 scrapy 项目中可能会有多个爬虫，name用于标识每个爬虫，不能相同

    def start_requests(self):
        """ 需要返回一个可迭代对象，迭代的元素是 'scrapy.Request'对象，可迭代对象可以是一个列表或者是迭代器，这样 scrapy 就知道哪些网页需要爬取。'scrapy.Request' 接受一个 url 参数和一个 callback 参数，url 指明要爬取的网页，callback是一个回调函数用于处理返回的网页，通常是一个提取数据的 parse 函数"""
        pass

    def parse(self, response):
        """ 这个方法作为 'scrapy.Request' 的 callback, 在这里编写提取数据的代码。scrapy 中的下载器会下载 start_reuqests 中动议的每个 'Request' 并且结果封装为一个 response 对象传入这个方法 """
        pass

