from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float

import datetime
from products_scraper import db_settings

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    site_product_id = Column(String)
    name = Column(String)
    brand = Column(String)
    categories = Column(String)
    description = Column(Text)
    url = Column(String)
    site = Column(String)

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    site_product_id = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    size = Column(String)
    color = Column(String)
    price = Column(Float)
    stock_state = Column(String)
    date = Column(DateTime)

Base.metadata.bind = db_settings.ENGINE
Base.metadata.create_all()


