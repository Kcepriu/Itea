from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from mongoengine import DoesNotExist

from .models import Products, Categories
from .schemas import ProductsSchema, CategoriesSchema, CostSchema


class ProductsResources(Resource):
    def get(self, product_id=None):
        if product_id:
            obj = Products.objects.get(id=product_id)
            obj.add_count()
            return ProductsSchema().dump(obj)

        objs = Products.objects()
        for obj in objs:
            obj.add_count()
        objs = Products.objects()
        return ProductsSchema().dump(objs, many=True)

    def post(self):
        try:
            res = ProductsSchema().load(request.get_json())
            obj = Products.objects.create(**res)
            return ProductsSchema().dump(obj)

        except ValidationError as err:
            return {'error': err.messages}

    def put(self, product_id):
        try:
            res = ProductsSchema().load(request.get_json())
            res['categorie'] = Categories.objects.get(id=res['categorie'])
            obj = Products.objects().get(id=product_id)
            obj.update(**res)
            return ProductsSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, product_id):
        product = Products.objects().get(id=product_id)
        product.delete()
        return {'status': 'deleted'}


class CategoriesResources(Resource):
    def get(self, categori_id=None):
        if categori_id:
            return CategoriesSchema().dump(Categories.objects.get(id=categori_id))
        return CategoriesSchema().dump(Categories.objects(), many=True)

    def post(self):
        try:
            res = CategoriesSchema().load(request.get_json())
            obj = Categories.objects.create(**res)
            return CategoriesSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, categori_id):
        try:
            res = CategoriesSchema().load(request.get_json())
            parent_id = res.get('parent', None)
            if parent_id:
                res['parent'] = Categories.objects.get(id=parent_id)
            else:
                res['parent'] = None
            obj = Categories.objects().get(id=categori_id)
            obj.update(**res)
            return CategoriesSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, categori_id):
        # Якщо є підкатегорії то не видаляти
        find_categorie = Categories.objects.filter(parent=categori_id)
        if find_categorie:
            return {'error': 'there are subcategories'}

        # Якщо є товари то не видаляти
        find_tovar = Products.objects.filter(categorie=categori_id)
        if find_tovar:
            return {'error': 'there is a product in the category'}

        categorie = Categories.objects().get(id=categori_id)
        categorie.delete()
        return {'status': 'deleted'}




class CostResources(Resource):
    def get(self, categori_id=None):
        if categori_id:
            sum_product = Products.objects(categorie=categori_id).aggregate([
                {'$group': {'_id': None, 'cost': {'$sum': {"$multiply": ["$count", "$price"]}}}}
            ])
        else:
            sum_product = Products.objects().aggregate([
                {'$group': {'_id': None, 'cost': {'$sum':  {"$multiply" : ["$count", "$price"]}}}}
            ])

        try:
            #  не знайшов як перевірити чи є в find_posts якісь записи
            result = sum_product.next()
        except StopIteration:
            return {'cost': 0}
        else:
            return CostSchema().dump(result)
