from marshmallow import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserSchema(ma.Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    token = fields.Str(dump_only=True)
    date_created = fields.DateTime(dump_only=True)

user_schema = UserSchema()

