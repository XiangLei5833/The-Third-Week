#-*- coding: utf-8 -*-

import sys
from sqlalchemy.orm import sessionmaker
sys.path.append('services')
from shiyanlou.models import Course, engine


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ parse 出来的item 会传递到这里，这里编写的处理代码会作用到每一个 item 上面。这个方法必须返回一个 item 对象 """
        item['students'] = int(item['students']) # 提取的学习人数是字符串，转化成int
        self.session.add(Course(**item))
        return item

    def open_spider(self, spider):
        """ 当爬虫开启的时候调用 """
        Session = sessionmaker(bind=engine)    # 创建数据库 session
        self.session = Session()

    def close_spider(self, spider):
        """ 当爬虫关闭的时候调用 """
        self.session.commit()    # 提交 session 然后关闭 session
        self.session.close()   

