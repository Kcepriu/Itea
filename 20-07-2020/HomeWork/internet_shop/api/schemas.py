from marshmallow import Schema, fields, validate

class  CategoriesSchema(Schema):
    id = fields.String(validate=validate.Length(min=24, max=24), dump_only=True)
    category_name = fields.String(validate=validate.Length(min=2, max=255), required=True)
    description = fields.String(validate=validate.Length(min=2, max=512))
    parent = fields.String(validate=validate.Length(min=0, max=24))


class ProductsSchema(Schema):
    id = fields.String(validate=validate.Length(min=24, max=24), dump_only=True)
    name = fields.String(validate=validate.Length(min=2, max=255), required=True)
    price = fields.Decimal(as_string=True)
    count = fields.Integer()
    count_viewing = fields.Integer(dump_only=True)
    availability = fields.Boolean()
    categorie = fields.String(validate=validate.Length(min=24, max=24), required=True)

class CostSchema(Schema):
    cost = fields.Decimal(as_string=True)
