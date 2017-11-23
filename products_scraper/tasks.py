from products_scraper.celery import app
from sqlalchemy.orm import sessionmaker
from products_scraper import db_settings, db_models


@app.task
def save_products(products):
    Session = sessionmaker(bind=db_settings.ENGINE)
    ses = Session()
    db_products = []
    for item in products:
        db_products.append(db_models.Product(id=item['id'],
                              site_product_id=item['site_product_id'],
                              name=item['name'],
                              brand=item['brand'],
                              categories=' '.join(item['categories']),
                              description=item['description'],
                              url=item['url'],
                              site=item['site']
                              ))
    ses.add_all(db_products)
    ses.commit()
    ses.close()


@app.task
def save_prices(prices):
    Session = sessionmaker(bind=db_settings.ENGINE)
    ses = Session()
    db_prices = []
    for item in prices:
        db_prices.append(db_models.Price(id=item['id'],
                                         site_product_id=item['site_product_id'],
                                         product_id=item['product_id'],
                                         size=item['size'],
                                         color=item['color'],
                                         price=item['price'],
                                         stock_state=item['stock_state'],
                                         date=item['date']
                                         ))
    ses.add_all(db_prices)
    ses.commit()
    ses.close()