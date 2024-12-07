from django.db.models import Count, F

from MUFC2.model import hobby
from MUFC2.model.friend import Friend
from MUFC2.model.hobby import Hobby
from MUFC2.model.user import User
from django.db.models import Count, Q


# Rank hobbies based on the popularity among each user's friend list
def hobby_rank_popularity(user_id):
    try:
        hobbies = (
            Hobby.objects.filter(friends__user_id=user_id)
            .annotate(friends_count=Count('friends'))
            .order_by('-friends_count')
        )
        return hobbies
    except Exception as e:
        print(f'Exception when ranking hobby: {e}')
        return None

# Get list of friends who have all hobbies in the provided hobby_list
def filter_friends_with_all_hobbies(user_id, hobby_list):
    try:
        # Filter friends belonging to the user, annotated with a count of hobbies that match hobby_list
        filtered_friends = (
            Friend.objects.filter(user_id=user_id, hobbies__name__in=hobby_list)
            .annotate(matching_hobby_count=Count('hobbies', filter=Q(hobbies__name__in=hobby_list)))
            .filter(matching_hobby_count=len(hobby_list))  # Only include friends with all hobbies in hobby_list
            .order_by("level_friendship")
        )
        return filtered_friends
    except Exception as e:
        print(f'Exception when filtering friends by all hobbies: {e}')
        return None

# Read the current hobbies that a specific friend has
def read_hobbies_from_friend(friend_id):
    try:
        # Since `hobbies` is now in `Friend`, we can directly access it
        friend = Friend.objects.get(pk=friend_id)
        return friend.hobbies.all()
    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return None
    except Exception as e:
        print(f'Exception when reading hobbies from friend: {e}')
        return None

# Add hobbies to one friend
def add_hobby_to_friend(friend_id, hobby_name):
    try:
        friend = Friend.objects.get(pk=friend_id)
        # Check if the hobby is already created
        hobby_get, created = Hobby.objects.get_or_create(name=hobby_name)
        # Check if the friend already has this hobby
        if friend.hobbies.filter(pk=hobby_get.pk).exists():
            print(f'Hobby {hobby_get.name} already exists for this friend')
            return False
        else:
            friend.hobbies.add(hobby_get)
            return True

    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return False
    except Exception as e:
        print(f'Exception when adding hobby to friend: {e}')
        return False

# Remove one hobby from friend:
def remove_hobby_from_friend(friend_id, hobby_name):
    try:
        friend = Friend.objects.get(pk=friend_id)
        hobby_get = Hobby.objects.get(name=hobby_name)  # Use get to retrieve the hobby without creating it
        if friend.hobbies.filter(pk=hobby_get.pk).exists():  # Check if hobby is associated with friend
            friend.hobbies.remove(hobby_get)
            friend.save()
            return True
        else:
            print(f'Hobby {hobby_get.name} is not associated with this friend')
            return False
    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return False
    except Hobby.DoesNotExist:
        print(f'Hobby {hobby_name} does not exist')
        return False
    except Exception as e:
        print(f'Exception when removing hobby from friend: {e}')
        return False






