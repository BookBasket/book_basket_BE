from app import db
from sqlalchemy.dialects.postgresql import JSON


class Book(db.Model):
	__tablename__ = 'books'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String())

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return '<id {}>'.format(self.id)


class Author(db.Model):
	__tablename__ = 'authors'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String())

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<id {}>'.format(self.id)

class Genre(db.Model):
	__tablename__ = 'genres'

	id = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.String())

	def __init__(self, type):
		self.type = type

	def __repr__(self):
		return '<id {}>'.format(self.id)

