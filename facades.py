from services import *
from popos import *

class SearchFacade():
	def	__init__(self, query):
		self.id = None
		self.query = query


	def books(self):
		collection = []
		for book in self.service().get_json()['items']:
			collection.append(Book(book))

		return collection


	def	service(self):
		return GoogleBooksService(self.query)