class Book:
	def __init__(self, object):
		self.title = object['volumeInfo'].setdefault('title', '')
		self.author = object['volumeInfo'].setdefault('authors', [])
		self.description = object['volumeInfo'].setdefault('description', '')
		self.published_date = object['volumeInfo'].setdefault('publishedDate', '')
		if 'imageLinks' in object['volumeInfo']:
			self.image_url = object['volumeInfo']['imageLinks'].setdefault('thumbnail', '')
		else:
			self.image_url = ''
		self.genres = object['volumeInfo'].setdefault('categories', [])