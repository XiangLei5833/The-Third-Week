# -*- coding: utf-8 -*-
import sys
import scrapy
sys.path.append('..')
from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']

    @property
    def start_urls(self):
        url_tmpl = 'http://shiyanlou.com/courses/?category=all&courses_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1, 23))

    def parse(self, response):
        for course in response.css('div.course-body'):
            item = CourseItem({
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                })
            yield item
