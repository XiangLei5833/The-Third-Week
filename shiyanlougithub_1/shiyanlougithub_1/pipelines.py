# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from shiyanlougithub.repositories import Repository, engine
from datetime import datetime

class ShiyanlougithubPipeline(object):

    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        item['commits'] = int(item['commits'][0])
        item['branches'] = int(item['branches'][0])
        item['releases'] = int(item['releases'][0])
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


