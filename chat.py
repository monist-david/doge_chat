from flask import Flask, render_template, request
from flask_restful import Api, Resource, abort, marshal_with, fields
from marshmallow import Schema
import marshmallow

app = Flask(__name__)
api = Api(app)

response_fields = {
    'text': fields.String,
}

class HumanSchema(Schema):
    text = marshmallow.fields.String()

class HumanReponse:
    def __init__(self, text):
        self.text = text


class BotResponse(Resource):
    @marshal_with(response_fields)
    def post(self):
        try:
            json_request = request.get_json()
            # human_schema = HumanSchema()
            # new_object = human_schema.load(json_request)

            text = HumanReponse(json_request)
            return text
        except:
            abort(404, message="Failed to make a response")

api.add_resource(BotResponse, '/response')


if __name__ == "__main__":
    app.run(debug=True)