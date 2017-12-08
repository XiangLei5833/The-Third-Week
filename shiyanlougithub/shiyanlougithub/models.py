# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Date, Column, Integer, String

engine = create_engine("mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8")
Base = declarative_base()

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(Date)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
