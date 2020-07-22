from marshmallow import Schema, fields, validate


class VehicleSchema(Schema):
    id = fields.String(dump_only=True)
    type_ = fields.String(validate=validate.Length(min=3, max=255))
    engine = fields.String(validate=validate.Length(min=3, max=255), required=True)
    manufacturer = fields.String(dump_only=True)
    colour = fields.String(validate=validate.OneOf(['Black','White']))