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

	# def test_search_endpoint_with_isbn(self):
	# 	response = self.app.get('/search?type=author&q=george rr martin')
	# 	self.assertEqual(200, response.status_code)
	#
	# 	json_data = json.loads(response.data)
	# 	self.assertEqual(40, len(json_data.get('data')))
	#
	# def test_search_endpoint_with_genre(self):
	# 	response = self.app.get('/search?type=author&q=george rr martin')
	# 	self.assertEqual(200, response.status_code)
	#
	# 	json_data = json.loads(response.data)
	# 	self.assertEqual(40, len(json_data.get('data')))





	def test_create_book_endpoint(self):
		response = self.app.post('/create_book?title=Testing3&author=J K Rowling&summary=This is a test&image_url=not_a_real_image.jpeg&isbn=0&published_date=May 7 2001&genre=fiction&genre=fantasy')
		self.assertEqual(200, response.status_code)

		json_data = json.loads(response.data)
		author_name = json_data['data']['attributes']['authors']['data'][0]['attributes']['name']
		self.assertEqual(author_name, 'J K Rowling')

	# def test_switch_shelves_endpoint(self):
	# 	self.app.post('/create_book?title=Testing3&author=J K Rowling&summary=This is a test&image_url=not_a_real_image.jpeg&isbn=123456&published_date=May 7 2001&genre=fiction&genre=fantasy')
	# 	response = self.app.patch('/switch_shelves?isbn=123456')
	#
	# 	self.assertEqual(200, response.status_code)
