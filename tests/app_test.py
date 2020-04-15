import unittest
import requests
import json
from app import app
# from models import *

class TestApp(unittest.TestCase):
	def setUp(self):
		app.config.from_object('config.TestingConfig')
		self.app = app.test_client()

	def test_root_page(self):
		response = self.app.get('/')
		self.assertEqual(200, response.status_code)

	def test_search_endpoint_with_author(self):
		response = self.app.get('/search?type=author&q=george rr martin')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		self.assertEqual(40, len(json_data.get('data')))

	def test_search_endpoint_with_title(self):
		response = self.app.get('/search?type=title&q=cloud atlas')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		self.assertEqual(40, len(json_data.get('data')))

	def test_search_endpoint_with_isbn(self):
		response = self.app.get('/search?type=isbn&q=0553103547')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		self.assertEqual(1, len(json_data.get('data')))

	def test_search_endpoint_with_genre(self):
		response = self.app.get('/search?type=genre&q=fiction')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		self.assertEqual(40, len(json_data.get('data')))
