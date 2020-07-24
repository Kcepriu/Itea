from flask import Flask
from flask_restful import Api

from .resources import PostResources, AuthorResources, TegResources, FindPostsResources

app = Flask(__name__)
api = Api(app)

api.add_resource(PostResources,     '/posts', '/posts/<post_id>')
api.add_resource(AuthorResources,   '/authors', '/authors/<author_id>')
api.add_resource(TegResources,      '/tegs', '/tegs/<teg_id>')

api.add_resource(FindPostsResources, '/find_posts/<teg_name>')