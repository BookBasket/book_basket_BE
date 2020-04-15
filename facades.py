from services import *
from popos import *

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
			new_book = Book.from_google_response(book)
			url = "http://covers.openlibrary.org/b/isbn/{}-M.jpg".format(new_book.isbn)
			new_book.image_url = url
			books.append(new_book)

		return cls(query, books)
