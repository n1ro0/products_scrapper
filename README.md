# products_scrapy
-From default category url It scrapped to my database 55138 products and 303255 product prices.

-To make this project work you have to start celery and lordandtaylor spider
 lordandtaylor spider crawls products and all possible product prices from chosen category.
 Celery saves it to postgres database. You have to run servers: 
 Redis, Postgres and create user and database in postgresql
	1. When you install redis server it automatically starts:
        sudo apt-get install redis-server

    2. When you install postgresql its server automatically starts:
        sudo apt-get install postgresql

    3. to create user and database use commands bellow:
        rsql
        CREATE USER scrapy_user with password 'qwerty12';
        CREATE DATABASE scrapy_db owner scrapy_user;

    4. to run scrapy worker:
        enter folder: products_scraper/products_scraper
        run command: celery -A products_scraper worker --loglevel=info

    5. to run spider:
        enter folder: products_scraper/products_scraper
        run command: scrapy crawl lordandtaylor


