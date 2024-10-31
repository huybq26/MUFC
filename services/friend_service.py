from MUFC.models.user import User


def get_friends_from_user(user_id):
    try:
        user = User.objects.get(pk=user_id)
        friends = user.friends.all()
        return friends
    except User.DoesNotExist:
        return []