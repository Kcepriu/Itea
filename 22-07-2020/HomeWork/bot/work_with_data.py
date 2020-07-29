from .models import User

class WorkWithData:
    @staticmethod
    def add_user(message):
        user = User.objects(user_id=message.id)
        if not user:
            user = User.objects.create(user_id=message.id, first_name=message.first_name,
                         last_name=message.last_name, username=message.username)
        return user