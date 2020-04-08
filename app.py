# Dependencies
from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_seeder import FlaskSeeder
from flask_graphql import GraphQLView
import json

# dotenv
from dotenv import load_dotenv
load_dotenv()

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
from models import *

# Schema
from schema import *

# POPOs
from popos import *

# Serializers
from serializers import *

# Facades
from facades import *

# Routes
@app.route('/')
def index():
    return 'Welcome to Book Basket'

app.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql = True
    )
)

@app.route('/search')
def search():
    payload = {
        'key': os.environ['GOOGLE_BOOKS_KEY'],
        'q': 'inauthor:george rr martin',
        'maxResults': 5
    }
    search = SearchFacade(payload)
    book_collection = search.books()
    serializer = BookSerializer(many = True)
    result = serializer.dump(book_collection)
    return jsonify(result)


if __name__ == '__main__':
     app.run()