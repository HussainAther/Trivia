from marshmallow import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TriviaSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    category = fields.Str(required=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    limit = fields.Int()

trivia_schema = TriviaSchema()
trivia_schemas = TriviaSchema(many=True)

