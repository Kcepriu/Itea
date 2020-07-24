from flask import Flask
from flask_restful import Api

from .resources import ProductsResources, CategoriesResources, CostResources

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductsResources,     '/products', '/products/<product_id>')
api.add_resource(CategoriesResources,    '/categories', '/categories/<categori_id>')
api.add_resource(CostResources,          '/cost', '/cost/<categori_id>')
