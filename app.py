# Dependencies
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import requests
from flask_seeder import FlaskSeeder

# app initialization
app = Flask(__name__)

# Configs
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Modules
db = SQLAlchemy(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)

# Models
from models import Book, Author, Genre, Shelf

# Schema Objects
# from schema_objects import BookObject

# Routes
@app.route('/')
def index():
    return 'Hello World'


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
     app.run()