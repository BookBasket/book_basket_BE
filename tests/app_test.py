import unittest
import requests
import json
from app import app

class TestApp(unittest.TestCase):
	def setUp(self):
		app.config.from_object('config.TestingConfig')
		self.app = app.test_client()

	def test_root_page(self):
		response = self.app.get('/')
		self.assertEqual(200, response.status_code)

	def test_search_endpoint(self):
		response = self.app.get('/search?type=author&q=george rr martin')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		self.assertEqual(40, len(json_data.get('data')))

	def test_create_book_endpoint(self):
		response = self.app.post('/create_book?title=Testing3&author=J K Rowling&summary=This is a test&image_url=not_a_real_image.jpeg&isbn=123456&published_date=May 7 2001&genre=fiction&genre=fantasy')
		self.assertEqual(200, response.status_code)
