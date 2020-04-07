from marshmallow import Schema, fields, pprint

class BookSerializer(Schema):
    title = fields.String()
    # authors = fields.List()
    description = fields.String()
    published_date = fields.String()
    image_url = fields.String()
    # genres = fields.List()