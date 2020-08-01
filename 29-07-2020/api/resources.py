from flask_restful import Resource
from .schemas import AuthorShema

class AuthorResources(Resource):
    def get(self, author_id=None):
        if author_id:
            return AuthorShema.dumps()

