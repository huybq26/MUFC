from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from MUFC.models.user import User

## Methods to get a user from attribute
def get_user_by_attribute(attribute, value):
    try:
        return User.objects.get(**{attribute: value})  # Use keyword argument unpacking
    except User.DoesNotExist:
        return None

## Methods to get a user's attributes
def get_user_attribute_from_id(user_id, attribute):
    try:
        user = User.objects.get(id=user_id)
        return getattr(user, attribute, None)  # Safely get the attribute value
    except User.DoesNotExist:
        return None

## Methods to get user from id
def get_user_from_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None

## Methods to create new user
def create_user(username, name, email, phone, password, dob, tele):
    try:
        hashed_password = make_password(password)
        user = User(username, name, email, phone, hashed_password, dob, tele)
        user.full_clean()
        user.save()
        return user
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

## Methods to update user's attributes from id
def update_user(user_id, attribute, value):
    try:
        user = User.objects.get(id=user_id)
        setattr(user, attribute, value)
        user.full_clean()
        user.save()
        return True
    except User.DoesNotExist:
        print(f"User {user_id} does not exist")
        return False
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return False
    except Exception as e:
        print(f"An exception occurred: {e}")
        return False


## Methods to delete a user
def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True

    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist")
        return False
    except Exception as e:
        print(f"An exception occurred: {e}")
        return False

def validate_user_password(user, raw_password):
    return user.check_password(raw_password)

## Methods to get a user's friends (maybe put in the friend service instead)

## Methods to get a user's hobbies (put in the hobby service)





