Create/Activate Virtual Environment
```
$ venv env --python=python3.7.7
$ source env/bin/activate
```

Install Requirements
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

$ python manage.py db init
$ python manage.py db migrate
```