from flask import Flask
app = Flask(__name__)
import os
from services import *
from popos import *
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# from app import db
# from dotenv import load_dotenv
from models import *
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# import schema
# from schema import *

class SearchFacade():
	def	__init__(self, query, books=[]):
		self.id = None
		self.query = query
		self.books = books

	@classmethod
	def from_query(cls, query):
		service = GoogleBooksService(query)
		books = []
		for book in service.get_json()['items']:
			books.append(Book.from_google_response(book))

		return cls(query, books)


class CreateBookFacade():
	def	__init__(self, args):
		self.id = None
		self.args = args


	def new_book(params):
		isbn=params.get('isbn')
		book = db.session.query(BookModel).filter_by(isbn=isbn).first()
		if book:
			return book
		else:
			shelf_id = params.get('shelf_id')
			shelf = ShelfModel.query.filter_by(id=shelf_id).first()

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

			title = params.get('title')
			summary = params.get('summary')
			image_url = params.get('image_url')
			isbn = params.get('isbn')
			published_date = params.get('published_date')

		book = BookModel(title=title, summary=summary, image_url=image_url, isbn=isbn, published_date=published_date, authors=authors, genres=genres, shelves=[shelf])
		db.session.add(book)
		db.session.commit()

		return book
