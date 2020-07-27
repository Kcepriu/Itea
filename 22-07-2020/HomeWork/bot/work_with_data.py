from .models import Users

class WorkWithData:
    def add_user(message):


        user = Users.objects(user_id=message.id)

        if not user:
            user = Users.objects.create(user_id=message.id, first_name=message.first_name,
                         last_name=message.last_name, username=message.username)
        return user