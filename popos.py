class Author:
	def __init__(self, name):
		self.name = name


class Genre:
	def __init__(self, type):
		self.type = type


class Book:
	def __init__(self, object):
		self.title = object['volumeInfo'].setdefault('title', '')
		self.description = object['volumeInfo'].setdefault('description', '')
		self.published_date = object['volumeInfo'].setdefault('publishedDate', '')

		if 'imageLinks' in object['volumeInfo']:
			self.image_url = object['volumeInfo']['imageLinks'].setdefault('thumbnail', '')
		else:
			self.image_url = ''

		self.author_list = object['volumeInfo'].setdefault('authors', [])
		self.authors = []
		for author in self.author_list:
			self.authors.append(Author(name=author))

		self.genre_list = object['volumeInfo'].setdefault('categories', [])
		self.genres = []
		for genre in self.genre_list:
			self.genres.append(Genre(type=genre))