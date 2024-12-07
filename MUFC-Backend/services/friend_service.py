from datetime import datetime, date, timedelta

from django.db.models import F, ExpressionWrapper, fields
from rest_framework.exceptions import ValidationError

from MUFC2.model.friend import Friend
from MUFC2.model.user import User

# Get list of friends
def get_friends_from_user(user_id):
    try:
        friends = Friend.objects.filter(user_id=user_id)
        return friends
    except User.DoesNotExist:
        return []
    except Exception as e:
        print(f'Exception when getting friend list: {e}')
        return []

# Get friend details
def get_friend_details(friend_id):
    try:
        friend = Friend.objects.get(pk=friend_id)
        return friend
    except Friend.DoesNotExist:
        return None
    except Exception as e:
        print(f'Exception when getting friend details: {e}')
        return None

# Add Friend with details
def add_friend(user_id, name, email, phone, dob, level_friendship, last_contacted, notes, facebook, whatsapp, insta, tele):
    try:
        user = User.objects.get(pk=user_id)
        friend = Friend(
            user_id = user,
            name = name,
            email = email,
            phone = phone,
            dob = dob,
            level_friendship = level_friendship,
            last_contacted = last_contacted,
            notes = notes,
            facebook = facebook,
            whatsapp = whatsapp,
            insta = insta,
            tele = tele,
            created_at = datetime.now(),
        )
        friend.full_clean()
        friend.save()
        return friend
    except ValidationError as e:
        print(f'Validation Error when adding friend: {e}')
        return None
    except Exception as e:
        print(f'Exception when adding friend: {e}')
        return None

# Modify all attributes of a friend
def update_friend_all_att(friend_id, fields_values):
    # fields_values is the dictionary where keys are field names and values are the new ones to set
    try:
        friend = Friend.objects.get(pk=friend_id)
        for field, value in fields_values.items():
            if hasattr(friend, field):
                setattr(friend, field, value)
        friend.full_clean()
        friend.save()
        return True
    except Friend.DoesNotExist:
        return False
    except ValidationError as e:
        print(f'Validation Error when updating friend: {e}')
        return False
    except Exception as e:
        print(f'Exception when updating friend: {e}')
        return False

# Delete friend method
def delete_friend(friend_id):
    try:
        friend = Friend.objects.get(pk=friend_id)
        friend.delete()
        return True
    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return False
    except Exception as e:
        print(f'Exception when deleting friend: {e}')
        return False

# Update friend with single attribute method
def update_friend_single_att(friend_id, attribute, value):
    try:
        friend = Friend.objects.get(pk=friend_id)
        setattr(friend, attribute, value)
        friend.full_clean()
        friend.save()
        return True
    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return False
    except ValidationError as e:
        print(f'Validation Error when updating friend: {e}')
        return False
    except Exception as e:
        print(f'Exception when updating friend: {e}')
        return False

# Rank friend based on level_friendship
def rank_friends_with_ordering(user_id, attribute, order):
    # possible attributes for sorting: level_friendship, last_contacted, name, created_at, DOB
    # order = 1 for ascending, and -1 for descending
    try:
        user = get_friend_details(user_id)

        # Handling dynamic ordering attribute
        if attribute == "dob":
            today = date.today()
            # Calculate the upcoming birthday based on this year or next year
            upcoming_birthday = ExpressionWrapper(
                F('dob').replace(year=today.year),
                output_field=fields.DateField()
            )
            # For friends who already had their birthday this year, set to next year
            friend_list = user.friends.annotate(
                upcoming_birthday=ExpressionWrapper(
                    F('dob').replace(year=today.year),
                    output_field=fields.DateField()
                ),
                days_until_birthday=ExpressionWrapper(
                    F('upcoming_birthday') - today,
                    output_field=fields.DurationField()
                )
            ).order_by(f"{'' if order == 1 else '-'}days_until_birthday")

        else:
            # General ordering for other fields
            ordering = f"{attribute}" if order == 1 else f"-{attribute}"
            friend_list = Friend.objects.filter(user_id=user_id).order_by(ordering)

        return friend_list
    except User.DoesNotExist:
        print(f"User {user_id} does not exist.")
        return []
    except Exception as e:
        print(f'Exception when getting friend list: {e}')
        return []

# List of friend that has the last_contacted for too long, or nearly too long
def should_promptly_contact_friend(user_id, expiration_period, notification_period):
    # expiration_period: default: 30 days -  the time needed to contact the friend from last_contacted.
    #   expiration_date = last_contacted + expiration_period
    # notification_period: default: 3 days - the time before expiration_date to notify the user
    try:
        friends = Friend.objects.filter(user_id=user_id)
        current_date = date.today()
        expiration_period = timedelta(days=int(expiration_period))
        notification_period = timedelta(days=int(notification_period))
        expired_list = friends.filter(last_contacted__lt=current_date - expiration_period)
        nearly_expired_list = friends.annotate(expiration_date=ExpressionWrapper(
                                    F('last_contacted') + expiration_period,
                                    output_field=fields.DateField()
                                )).filter(
                                    expiration_date__gt=current_date,
                                    expiration_date__lt=current_date + notification_period
                                )
        return expired_list | nearly_expired_list
    except User.DoesNotExist:
        print(f"User {user_id} does not exist.")
        return []
    except Exception as e:
        print(f'Exception when getting prompty contacted friend list: {e}')
        return []






