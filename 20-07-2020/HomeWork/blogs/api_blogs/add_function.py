import mongoengine as me
from .models import Post, Author, Teg

class AddFunction:
    @staticmethod
    def get_post_from_teg(teg_id):
        # Шукаю всі документи де викоритовується такий тег
        return Post.objects().aggregate([
                        {'$unwind': '$teg'},
                        {'$match': {'teg.teg': teg_id}},
                        {'$group': {'_id': '$_id'}}
                    ])

    @staticmethod
    def recursive_rename_teg_from_posts(teg_, teg_name):
        # Шукаю всі пости де використовується такий тег і змінюю його назву і там
        find_posts = AddFunction.get_post_from_teg(teg_.id)

        for post in find_posts:
            obj_post = Post.objects().get(id=post['_id'])
            find_tegs = obj_post.teg.filter(teg=teg_)
            for teg_obj in find_tegs:
                teg_obj.teg_name = teg_name
            obj_post.save()

    @staticmethod
    def get_get_post_from_author(author_id):
        return Post.objects().filter(author=author_id)

    @staticmethod
    def recursive_rename_author_from_posts(author_id, author_name):
        find_posts = AddFunction.get_get_post_from_author(author_id)
        for obj_post in find_posts:
            obj_post.author_name = author_name
            obj_post.save()

    @staticmethod
    def count_publication_author(author_id):
        return Post.objects().filter(author=author_id).count()

    @staticmethod
    def add_tegs(obj_post, res):
        for elem in res:
            obj_teg = Teg.objects.get(id=elem['teg'])
            obj_post.teg.create(teg=obj_teg, teg_name=obj_teg.teg_name)

    @staticmethod
    def add_post(dict_data):
        kwargs = dict_data.copy()
        tegs = kwargs.pop('teg')

        obj_author = Author.objects.get(id=kwargs['author'])
        kwargs['author_name'] = f'{obj_author.first_name} {obj_author.sur_name}'

        new_post = Post.objects.create(**kwargs)

        AddFunction.add_tegs(new_post, tegs)

        new_post.save()

        return new_post

    @staticmethod
    def update_post(obj, dict_data):
        kwargs = dict_data.copy()
        tegs = kwargs.pop('teg')

        obj_author = Author.objects.get(id=kwargs['author'])
        kwargs['author'] = obj_author
        kwargs['author_name'] = f'{obj_author.first_name} {obj_author.sur_name}'

        obj.teg.clear()
        obj.update(**kwargs)

        AddFunction.add_tegs(obj, tegs)

        obj.save()
