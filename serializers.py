from marshmallow_jsonapi import Schema, fields

class BookSerializer(Schema):
    id = fields.String()
    title = fields.String()
    authors = fields.String()
    description = fields.String()
    published_date = fields.String()
    image_url = fields.String()
    genres = fields.String()

    class Meta:
        type_ = 'book'


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