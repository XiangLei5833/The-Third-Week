# -*- coding: utf-8 -*-
import scrapy
from courses_follow.items import CoursesImageItem

class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        item = CoursesImageItem()
        item['image_urls'] = response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item
