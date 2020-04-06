from app import db
from sqlalchemy.dialects.postgresql import JSON


class Book(db.Model):
	__tablename__ = 'books'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String())
	authors = db.relationship('Author', secondary='book_authors', backref=db.backref('books'))
	genres = db.relationship('Genre', secondary='book_genres', backref=db.backref('books'))
	shelves = db.relationship('Shelf', secondary='book_shelves', backref=db.backref('books'))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return f'<Book(id: {self.id}, title: {self.title})>'


class Author(db.Model):
	__tablename__ = 'authors'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String())

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'<Author(id: {self.id}, name: {self.name})>'


class Genre(db.Model):
	__tablename__ = 'genres'

	id = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.String())

	def __init__(self, type):
		self.type = type

	def __repr__(self):
		return f'<Genre(id: {self.id}, type: {self.type})>'


class Shelf(db.Model):
	__tablename__ = 'shelves'

	id = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.String())

	def __init__(self, type):
		self.type = type

	def __repr__(self):
		return f'<Shelf(id: {self.id}, type: {self.type})>'


book_authors = db.Table('book_authors',
			db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
			db.Column('author_id', db.Integer, db.ForeignKey('authors.id'))
			)


book_genres = db.Table('book_genres',
			db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
			db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
			)


book_shelves = db.Table('book_shelves',
			db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
			db.Column('shelf_id', db.Integer, db.ForeignKey('shelves.id'))
			)
