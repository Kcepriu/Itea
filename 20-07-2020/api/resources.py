from flask_restful import Resource
from flask import request
from models import User
import json

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            return json.loads(User.objects(id=user_id).to_json())

        return json.loads(User.objects().to_json())

    def post(self):
        user = User.objects.create(**request.json)
        return json.loads(user.to_json())

    def put(self):
        pass

    def delete(self, user_id):
        User.objects(id=user_id).delete()


