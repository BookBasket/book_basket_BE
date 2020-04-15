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
			books.append(Book.from_google_response(book))

		return cls(query, books)