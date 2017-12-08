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
            item = GithubItem({
                    "name": content.xpath('.//div[1]/h3/a/text()').re_first('(\w+)'),
                    "update_time": content.xpath('.//div[3]/relative-time/@datetime').extract_first()
                    })
            repository_url = response.urljoin(content.xpath('.//div[1]/h3/a/@href').extract_first())
            request = scrapy.Request(repository_url, callback=self.parse_content)
            request.meta['item'] = item
            yield request

    def parse_content(self, response):
        item = response.meta['item']
        for substance in response.xpath('//ul[@class="numbers-summary"]'):
          
            item['commits'] = substance.xpath('.//li[1]/a/span/text()').re_first('(\w+)'),
            item['branches'] = substance.xpath('.//li[2]/a/span/text()').re_first('(\w+)'),
            item['releases'] = substance.xpath('.//li[3]/a/span/text()').re_first('(\w+)')
            yield item
