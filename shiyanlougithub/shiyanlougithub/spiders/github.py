#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import scrapy
from shiyanlougithub.items import GithubItem

class GithubSpider(scrapy.Spider):

    name = 'github'

    @property
    def start_urls(self):
        github_url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (github_url.format(i) for i in range(1,5))

    def parse(self, response):
        for content in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield GithubItem({
                    "name": content.xpath('.//div[1]/h3/a/text()').re_first('(\w+)'),
                    "update_time": content.xpath('.//div[3]/relative-time/@datetime').extract_first()
                    })
