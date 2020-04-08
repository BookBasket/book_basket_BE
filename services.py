import requests
import json

class GoogleBooksService():
	def __init__(self, query):
		self.query = query


	def get_json(self):
		response = requests.get('https://www.googleapis.com/books/v1/volumes', params = self.query)
		return json.loads(response.content)
