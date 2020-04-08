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
		response = self.app.get('/search?type=inauthor:&q=george rr martin')
		self.assertEqual(200, response.status_code)
