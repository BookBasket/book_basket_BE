Requirements
- Python 3.7.7
- PSQL 11.5

Clone Repository
```
git clone git@github.com:BookBasket/book_basket_BE.git
```

Navgiate to Repository
```
cd book_basket_BE
```

Create/Activate Virtual Environment
```
$ python3 -m venv env
$ source env/bin/activate
```

Install Dependencies
```
$ pip install -r requirements.txt
```

Set Local Variables
```
$ export APP_SETTINGS="config.DevelopmentConfig"
$ export DATABASE_URL="postgresql:///book_basket_dev"
```

Create/Migrate Database
```
$ psql
# create database book_basket_dev;
CREATE DATABASE
# \q

$ python manage.py db upgrade
```
