#!/usr/bin/env python3

import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    """ ���� scrapy ������Ҫдһ�� Spider �࣬�����̳� scrapy.Spider �ࡣ��������ж���Ҫ�������վ�����ӣ��Լ���δ���ҳ�з������ݵ�"""

    name = 'shiyanlou-courses'    # �����ʶ���ţ��� scrapy ��Ŀ�п��ܻ��ж�����棬name���ڱ�ʶÿ�����棬������ͬ

    def start_requests(self):
        """ ��Ҫ����һ���ɵ������󣬵�����Ԫ���� 'scrapy.Request'���󣬿ɵ������������һ���б�����ǵ����������� scrapy ��֪����Щ��ҳ��Ҫ��ȡ��'scrapy.Request' ����һ�� url ������һ�� callback ������url ָ��Ҫ��ȡ����ҳ��callback��һ���ص��������ڴ����ص���ҳ��ͨ����һ����ȡ���ݵ� parse ����"""
        pass

    def parse(self, response):
        """ ���������Ϊ 'scrapy.Request' �� callback, �������д��ȡ���ݵĴ��롣scrapy �е������������� start_reuqests �ж����ÿ�� 'Request' ���ҽ����װΪһ�� response ������������� """
        pass

