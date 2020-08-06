from marshmallow import Schema, fields

class AuthorShema(Schema):
    id = fields.String(dump_only=True)
    login = fields.String()
    password = fields.String(load_only=True)
    post = fields.String()

