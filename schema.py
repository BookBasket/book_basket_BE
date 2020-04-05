from models import *
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene


class BookObject(SQLAlchemyObjectType):
	class Meta:
		model = Book
		interfaces = (graphene.relay.Node,)


class AuthorObject(SQLAlchemyObjectType):
	class Meta:
		model = Author
		interfaces = (graphene.relay.Node,)


class GenreObject(SQLAlchemyObjectType):
	class Meta:
		model = Genre
		interfaces = (graphene.relay.Node,)


class ShelfObject(SQLAlchemyObjectType):
	class Meta:
		model = Shelf
		interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()

	book = graphene.relay.Node.Field(BookObject)
	all_books = SQLAlchemyConnectionField(BookObject)

	author = graphene.relay.Node.Field(AuthorObject)
	all_authors = SQLAlchemyConnectionField(AuthorObject)

	genre = graphene.relay.Node.Field(GenreObject)
	all_genres = SQLAlchemyConnectionField(GenreObject)

	shelf = graphene.relay.Node.Field(ShelfObject)
	all_shelves = SQLAlchemyConnectionField(ShelfObject)


schema = graphene.Schema(query=Query)