# Dependencies
from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_seeder import FlaskSeeder
from flask_graphql import GraphQLView
import json

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
    payload = {'key': 'AIzaSyDy_PYvNB25ePStZ4AgiSd8ZxIGcEpaZ4o', 'q': 'inauthor:george rr martin' }
    response = requests.get('https://www.googleapis.com/books/v1/volumes', params = payload)
    json_response = json.loads(response.content)
    books = json_response['items']
    book = books[0]
    return jsonify(
        title = book['volumeInfo']['title'],
        author = book['volumeInfo']['authors'],
        description = book['volumeInfo']['description'],
        published_date = book['volumeInfo']['publishedDate'],
        image = book['volumeInfo']['imageLinks']['thumbnail'],
    )


if __name__ == '__main__':
     app.run()