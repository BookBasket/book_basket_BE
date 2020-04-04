from flask_seeder import Seeder, Faker, generator
from models import Book, Author

class BookBasketSeeder(Seeder):
	def run(self):
		books = Faker(
			cls = Book,
			init = {
				"title": generator.String("Book [A-Z][a-z]{4}")
			}
		)

		authors = Faker(
			cls = Author,
			init = {
				"name": generator.Name()
			}
		)

		for book in books.create(20):
			print(f"Adding book: {book.title}")
			self.db.session.add(book)

		for author in authors.create(8):
			print(f"Adding author: {author.name}")
			self.db.session.add(author)