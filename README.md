Requirements
- Python 3.7.7
- PSQL 11.5

Clone Repository
```
$ git clone git@github.com:BookBasket/book_basket_BE.git
```

Create/Activate Virtual Environment
```
$ cd book_basket_BE
$ python3 -m venv env
$ source env/bin/activate
```

Install Dependencies
```
$ pip install -r requirements.txt
```

Create/Migrate Database
```
$ psql
# create database book_basket_dev;
CREATE DATABASE
# \q

$ python manage.py db upgrade
```
