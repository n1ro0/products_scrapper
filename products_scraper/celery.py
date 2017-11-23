from celery import Celery


app = Celery('products_scraper', broker='redis://', include=['products_scraper.tasks'])



