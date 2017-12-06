# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from sqlalchemy.orm import sessionmaker
sys.path.append('services')
from userdata.models import User, engine
from userdata.items import UserItem

class UserdataPipeline(object):
    def process_item(self, item, spider):
        item['level'] = int(item['level'][1:])
        item['join_date'] = datetime.striptime(item['join_date'].split()[0], '%Y-%m-%d').date()
        item['learn_courses_num'] = int(item['learn_courses_num'])
        self.session.add(User(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
