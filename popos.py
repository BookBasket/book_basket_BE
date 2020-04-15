class Author:
	def __init__(self, name):
		self.name = name


class Genre:
	def __init__(self, type):
		self.type = type


class Book:
	def __init__(self, id, title, description, published_date, image_url, isbn, authors, genres):
		self.id = id
		self.title = title
		self.description = description
		self.published_date = published_date
		self.isbn = isbn
		self.image_url = image_url
		self.authors = authors
		self.genres = genres

	@classmethod
	def from_google_response(cls, payload):
		book_data = payload['volumeInfo']

		id = payload['id']
		title = book_data.setdefault('title', '')
		description = book_data.setdefault('description', '')
		published_date = book_data.setdefault('publishedDate', '')

		if 'industryIdentifiers' in book_data:
			isbn = book_data['industryIdentifiers'][0].setdefault('identifier', '')
		else:
			isbn = ''

		if 'imageLinks' in book_data:
			image_url = book_data['imageLinks'].setdefault('thumbnail', '')
		else:
			image_url = ''

		authors = []
		for author in book_data.setdefault('authors', []):
			authors.append(Author(name=author))

		genres = []
		for genre in book_data.setdefault('categories', []):
			genres.append(Genre(type=genre))

		return cls(id, title, description, published_date, image_url, isbn, authors, genres)
