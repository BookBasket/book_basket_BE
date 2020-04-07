# import collections

# defd = collections.defaultdict(lambda : [])

class Book:
	def __init__(self, object):
		self.title = object['volumeInfo'].setdefault('title', '')
		self.author = object['volumeInfo'].setdefault('authors', [])
		self.description = object['volumeInfo'].setdefault('description', '')
		self.published_date = object['volumeInfo'].setdefault('publishedDate', '')
		self.image_url = object['volumeInfo'].setdefault('imageLinks', {})
		self.genres = object['volumeInfo'].setdefault('categories', [])