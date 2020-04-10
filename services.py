import requests
import json
import os

class GoogleBooksService():
	def __init__(self, query):
		self.query = query


	def get_json(self):
		type = self.query.get('type')
		if type == 'author':
			type = 'inauthor:'
		elif type == 'title':
			type = 'intitle:'
		elif type == 'genre':
			type = 'subject:'
		elif type == 'isbn':
			type = 'isbn:'

		query = self.query.get('q')

		payload = {
			'key':          os.environ['GOOGLE_BOOKS_KEY'],
			'q':            f'{type}{query}',
			'maxResults':   40,
			'printType':    'books'
		}
		response = requests.get('https://www.googleapis.com/books/v1/volumes', params = payload)
		return json.loads(response.content)
