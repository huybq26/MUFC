from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from MUFC2.model.user import User

## Methods to get a user from attribute
def get_user_by_attribute(attribute, value):
    try:
        return User.objects.get(**{attribute: value})  # Use keyword argument unpacking
    except User.DoesNotExist:
        return None

## Methods to get a user's attributes
def get_user_attribute_from_id(source_id, attribute):
    try:
        user = User.objects.get(user_id=source_id)
        return getattr(user, attribute, None)  # Safely get the attribute value
    except User.DoesNotExist:
        return None

## Methods to get user from id
def get_user_from_id(source_id):
    try:
        user = User.objects.get(user_id=source_id)
        return user
    except User.DoesNotExist:
        return None

## Methods to create new user
def create_user(username, name, email, phone, password, dob, tele):
    try:
        hashed_password = make_password(password)
        user = User(
            username=username,
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            dob=dob,
            tele=tele
        )
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
def update_user(source_id, attribute, value):
    try:
        user = User.objects.get(user_id=source_id)
        setattr(user, attribute, value)
        user.full_clean()
        user.save()
        return True
    except User.DoesNotExist:
        print(f"User {source_id} does not exist")
        return False
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return False
    except Exception as e:
        print(f"An exception occurred: {e}")
        return False

## Methods to update all attributes at once:
def update_all_user_fields(source_id, field_values):
    """
    Parameters:
    - user_id: UUID of the user to update
    - field_values: Dictionary where keys are field names and values are the new values to set
    """
    try:
        user = User.objects.get(user_id=source_id)
        for field, value in field_values.items():
            if hasattr(user, field):  # Ensure the user has the attribute before setting it
                setattr(user, field, value)
        user.full_clean()
        user.save()
        return True
    except User.DoesNotExist:
        return False

## Methods to delete a user
def delete_user(source_id):
    try:
        user = User.objects.get(user_id=source_id)
        user.delete()
        return True

    except User.DoesNotExist:
        print(f"User with ID {source_id} does not exist")
        return False
    except Exception as e:
        print(f"An exception occurred: {e}")
        return False

def validate_user_password(user, raw_password):
    return user.check_password(raw_password)

## Methods to get a user's friends (maybe put in the friend service instead)

## Methods to get a user's hobbies (put in the hobby service)





