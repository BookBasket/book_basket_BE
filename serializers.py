from marshmallow_jsonapi import Schema, fields

class AuthorSerializer(Schema):
    id = fields.String()
    name = fields.String()

    class Meta:
        type_ = 'author'


class GenreSerializer(Schema):
    id = fields.String()
    type = fields.String()

    class Meta:
        type_ = 'genre'


class BookSerializer(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    published_date = fields.String()
    image_url = fields.String()
    authors = fields.Nested(AuthorSerializer(), many=True)
    genres = fields.Nested(GenreSerializer(), many=True)

    class Meta:
        type_ = 'book'

