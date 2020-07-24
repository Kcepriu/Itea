import mongoengine as me
from .models import Post, Author, Tegs

class AddFunction:
    def get_post_from_teg(teg_id):
        # Шукаю всі документи де викоритовується такий тег
        return Post.objects().aggregate([
                        {'$unwind': '$teg'},
                        {'$match': {'teg.teg': teg_id}},
                        {'$group': {'_id': '$_id'}}
                    ])


    def recursive_rename_teg_from_posts(teg_, teg_name):
        # Шукаю всі пости де використовується такий тег і змінюю його назву і там
        find_posts = AddFunction.get_post_from_teg(teg_.id)

        for post in find_posts:
            obj_post = Post.objects().get(id=post['_id'])
            find_tegs = obj_post.teg.filter(teg=teg_)
            for teg_obj in find_tegs:
                teg_obj.teg_name = teg_name
            obj_post.save()

    def get_get_post_from_author(author_id):
        return Post.objects().filter(author=author_id)


    def recursive_rename_author_from_posts(author_id, author_name):
        find_posts = AddFunction.get_get_post_from_author(author_id)
        for obj_post in find_posts:
            obj_post.author_name = author_name
            obj_post.save()

    def count_publication_author(author_id):
        return Post.objects().filter(author=author_id).count()











