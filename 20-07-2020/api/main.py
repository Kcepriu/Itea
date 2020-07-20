from flask import Flask
from flask_restful import Api
from resources import UserResource

app = Flask(__name__)

api = Api(app)

api.add_resource(UserResource, '/users', '/users/<string:user_id>')

def start_server():
    app.run(debug=True)