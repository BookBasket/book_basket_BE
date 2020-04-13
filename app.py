# Dependencies
from flask import Flask, jsonify, request, make_response
import os
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_graphql import GraphQLView
import json
from flask_bcrypt import Bcrypt


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
bcrypt = Bcrypt(app)

# Schema
import schema
from schema import *

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

@app.route('/search', methods=['OPTIONS', 'GET'])
def search():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'GET':
        req = request.get_json()
        search = SearchFacade.from_query(request.args)
        book_collection = search.books
        serializer = BookSerializer(many = True)
        result = serializer.dump(book_collection)
        return build_actual_response(jsonify(result))

@app.route('/create_book', methods=['OPTIONS', 'POST'])
def create_book():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'POST':
        req = request.get_json()

        params = request.args
        shelf_id = params.get(shelf_id)
        shelf = Shelves.query.filter_by(id=shelf_id)

        title = params.get(title)
        summary = params.get(summary)
        image_url = params.get(image_url)
        isbn = params.get(isbn)
        published_date = params.get(published_date)

        book = BookModel(title=title, summary=summary, image_url=image_url, isbn=isbn, published_date=published_date)
        shelf.books.append(book)

        params.get(author)
        params.get(genre)
        # shelf = Shelves.query.filter_by(id=)


        # args:
        # shelf_id (find shelf with this)
        # book information (create book with this, associated with above shelf)
        # author information (check/create author, associate with book)
        # genre information (check/create genre, associate with book)





        search = SearchFacade.from_query(request.args)
        book_collection = search.books
        serializer = BookSerializer(many = True)
        result = serializer.dump(book_collection)
        return build_actual_response(jsonify(result))



def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run()
