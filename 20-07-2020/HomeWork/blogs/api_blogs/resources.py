from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from mongoengine import DoesNotExist

from .models import Post, Author, Teg
from .schemas import PostSchema, TegsSchema, AuthorSchema
from .add_function import AddFunction

class PostResources(Resource):
    def get(self, post_id=None):
        if post_id:
            obj = Post.objects.get(id=post_id)
            obj.add_count()

            return PostSchema().dump(obj)

        objs = Post.objects()
        for obj in objs:
            obj.add_count()
        objs = Post.objects()
        return PostSchema().dump(objs, many=True)

    def post(self):
        try:
            res = PostSchema().load(request.get_json())
            obj = AddFunction.add_post(res)
            return TegsSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, post_id):
        try:
            res = PostSchema().load(request.get_json())
            obj = Post.objects().get(id=post_id)
            AddFunction.update_post(obj, res)
            return PostSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}


    def delete(self, post_id):
        post = Post.objects().get(id=post_id)
        post.delete()
        return {'status': 'deleted'}

class AuthorResources(Resource):
    def get(self, author_id=None):
        if author_id:
            result = AuthorSchema().dump(Author.objects.get(id=author_id))
            result['count_publication'] = AddFunction.count_publication_author(author_id)
        else:
            result = AuthorSchema().dump(Author.objects(), many=True)
            for elem in result:
                elem['count_publication'] = AddFunction.count_publication_author(elem['id'])
        return result

    def post(self):
        try:
            res = AuthorSchema().load(request.get_json())
            obj = Author.objects.create(**res)
            return AuthorSchema().dump(obj)

        except ValidationError as err:
            return {'error': err.messages}

    def put(self, author_id):
        # треба знайти список документів де використовується цей автор. Змінити назву і в них
        try:
            res = AuthorSchema().load(request.get_json())
            author = Author.objects().get(id=author_id)
            author.update(**res)

            AddFunction.recursive_rename_author_from_posts(author_id, f'{author.first_name} {author.sur_name}')

            return AuthorSchema().dump(author.reload())

        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, author_id):
        # треба знайти список документів авотром яких являється вибраний обʼєкт
        find_author = AddFunction.get_get_post_from_author(author_id)
        if  find_author:
            # Можливо треба вернути якийсь код помилки???
            return {'error': 'Є пости в які написав даний автор'}

        author = Author.objects().get(id=author_id)
        author.delete()
        return {'status': 'deleted'}

class TegResources(Resource):
    def get(self, teg_id=None):
        if teg_id:
            return TegsSchema().dump(Teg.objects.get(id=teg_id))
        return TegsSchema().dump(Teg.objects(), many=True)

    def post(self):
        try:
            res = TegsSchema().load(request.get_json())
            obj = Teg.objects.create(**res)
            return TegsSchema().dump(obj)

        except ValidationError as err:
            return {'error': err.messages}

    def put(self, teg_id):
        # треба знайти список документів де використовується цей тег. Змінити назву і в них
        try:
            res = TegsSchema().load(request.get_json())
            teg = Teg.objects().get(id=teg_id)
            teg.update(**res)

            AddFunction.recursive_rename_teg_from_posts(teg, teg.teg_name)

            return TegsSchema().dump(teg.reload())

        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, teg_id):
        #треба знайти список документів де використовується цей тег. Якщо такий є то не видаляємо
        teg = Teg.objects().get(id=teg_id)

        find_posts = AddFunction.get_post_from_teg(teg.id)
        try:
            #  не знайшов як перевірити чи є в find_posts якісь записи
            find_posts.next()
        except StopIteration:
            pass
        else:
            # Можливо треба вернути якийсь код помилки???
            return {'error': 'Є пости в яких використовується даний тег'}

        teg.delete()
        return {'status': 'deleted'}

class FindPostsResources(Resource):
    def get(self, teg_name):
        try:
            teg = Teg.objects.get(teg_name=teg_name)
        except DoesNotExist as err:
            return {'error': 'Не найден такой тег'}


        find_posts = AddFunction.get_post_from_teg(teg.id)
        result = []
        for post in find_posts:
            result.append(Post.objects().get(id=post['_id']))
        return PostSchema().dump(result, many=True)




