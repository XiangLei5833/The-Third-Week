# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from userdata.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']
   
    @property
    def start_urls(self): 
        url_tmpl = 'http://www.shiyanlou.com/user/{}/'
        return (url_tmpl.format(i) for i in range(525000, 524800, -10))

    def parse(self, response):
        yield UserItem({
            'name': response.xpath('//span[@class="username"]/text()').extract_first(),
            'type': response.xpath('//a[@class="member-icon"]/img[@class="user-icon"]/@title').extract_first(default='普通用户'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'join_date': response.xpath('//span[@class="join=date"]/text()').extract_first(),
            'level': response.xpath('//span[@class="user-level"]/text()').extract_first(),
            'learn_courses_num':response.xpath('//span[@class="latest-learn-num"]/text()').extract_first
            })
