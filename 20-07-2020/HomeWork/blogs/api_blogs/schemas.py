from marshmallow import Schema, fields, validate

class  TegFieldSchema(Schema):
    teg = fields.String(validate=validate.Length(min=24, max=24))
    teg_name = fields.String(validate=validate.Length(min=2, max=255),  dump_only=True)

class PostSchema(Schema):
    id = fields.String(validate=validate.Length(min=24, max=24), dump_only=True)

    name = fields.String(validate=validate.Length(min=2, max=255))
    body = fields.String(validate=validate.Length(min=8, max=512), required=True)

    author = fields.String(validate=validate.Length(min=24, max=24))
    author_name = fields.String(validate=validate.Length(min=1, max=256), required=True, dump_only=True)

    count_viewing = fields.Integer(dump_only=True)

    date_publication = fields.DateTime(format='%d-%m-%Y')

    teg = fields.Nested(TegFieldSchema(many=True))


class TegsSchema(Schema):
    id = fields.String(dump_only=True)
    teg_name = fields.String(validate=validate.Length(min=2, max=255), required=True)

class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=validate.Length(min=1, max=256), required=True)
    sur_name = fields.String(validate=validate.Length(min=1, max=256), required=True)

