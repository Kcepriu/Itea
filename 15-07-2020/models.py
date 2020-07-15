import mongoengine as me
import datetime

me.connect('lesson_9_db')
class Post(me.Document):
    title = me.StringField(required=True)
    body = me.StringField(required=True)
    created = me.DateTimeField(default=datetime.datetime.now)


class User(me.Document):
    first_name = me.StringField(min_length=1, max_length=255, required=True)
    sur_name = me.StringField(min_length=1, max_length=255)
    interes = me.ListField(me.StringField(min_length=2, max_length=512))
    age = me.IntField()
    post = me.ReferenceField(Post)

    def __str__(self):
        return self.first_name


if __name__ == '__main__':
    # user = User(first_name='Serhii', sur_name='Kost', age=42, interes=['footbol', 'Programing'])
    # user.save()

    # user = User(first_name='Jull', sur_name='Bozdugan', age=30, interes=['Teatrs', 'Cinema'])
    # user.save()

    # user = User(first_name='Bred', sur_name='Pit', age=50, interes=['Teatrs', 'Cinema', 'Sex'])
    # user.save()

    #User.object.create(first_name='Serhii', sur_name='Kost', age=42, interes=['footbol', 'Programing'])

    users = User.objects(age__ne=10)
    # users = User.objects(interes__in=['Sex'])
    # users = User.objects.filter(age__gt=30)
    post = Post.objects.create(title='news', body='Text posts')
    user = User(first_name='Mike', sur_name='Tayson', age=40, interes=['footbol', 'Basketbol'], post = post)
    user.save()

    # for user in users:
    #     print(user.id, user.first_name, user.interes, user.age)
    #     # user.age += 1
    #     # user.save()

    # print(users)
    # print(user.id, user.age, user.first_name, user.sur_name, user.interes)

    print(user.first_name, user.post.title, user.post.body, user.post.created)


