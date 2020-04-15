# Dependencies
from flask import Flask, jsonify, request, make_response
import os
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_graphql import GraphQLView
import json
from flask_bcrypt import Bcrypt
from flask_cors import CORS

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
CORS(app)

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
    req = request.get_json()
    search = SearchFacade.from_query(request.args)
    book_collection = search.books
    serializer = BookSerializer(many = True)
    result = serializer.dump(book_collection)
    return jsonify(result)

@app.route('/create_book', methods=['OPTIONS', 'POST'])
def create_book():
    params = request.args
    isbn = params.get('isbn')
    book = db.session.query(BookModel).filter_by(isbn=isbn).first()
    if book:
        serializer = BookSerializer()
        result = serializer.dump(book)
        return build_actual_response(jsonify(result))
    else:
        params = request.args
        shelf = ShelfModel.query.filter_by(id=2).first()

        author_names = params.getlist('author')
        authors = []
        for author_name in author_names:
            author_object = db.session.query(AuthorModel).filter_by(name=author_name).first()
            if author_object:
                authors.append(author_object)
            else:
                created_author = AuthorModel(name=author_name)
                db.session.add(created_author)
                authors.append(created_author)


        genre_types = params.getlist('genre')
        genres = []
        for genre_type in genre_types:
            genre_object = db.session.query(GenreModel).filter_by(type=genre_type).first()
            if genre_object:
                genres.append(genre_object)
            else:
                created_genre = GenreModel(type=genre_type)
                db.session.add(created_genre)
                genres.append(created_genre)

        title = params.setdefault('title', '')
        summary = params.setdefault('summary', '')
        image_url = params.setdefault('image_url', '')
        isbn = params.setdefault('isbn', '')
        published_date = params.setdefault('published_date', '')
        book = BookModel(title=title, summary=summary, image_url=image_url, isbn=isbn, published_date=published_date, authors=authors, genres=genres, shelves=[shelf])
        db.session.add(book)
        db.session.commit()
        serializer = BookSerializer()
        result = serializer.dump(book)
        return jsonify(result)


@app.route('/switch_shelves', methods=['OPTIONS', 'PATCH'])
def switch_shelves():
    isbn = request.args.get('isbn')
    book = db.session.query(BookModel).filter_by(isbn=isbn).first()
    book.shelves.pop(0)
    shelf = db.session.query(ShelfModel).filter_by(id=1).first()
    book.shelves.append(shelf)

    db.session.add(book)
    db.session.commit()
    serializer = BookSerializer()
    result = serializer.dump(book)
    return jsonify(result)


# def build_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response


# def build_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

if __name__ == '__main__':
    app.run()
