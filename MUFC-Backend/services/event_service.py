# Create each event
from datetime import datetime

from MUFC2.model.event import Event
from MUFC2.model.friend import Friend
from MUFC2.model.user import User

# Create event with attributes
def create_event(name, date, user_id, friend_id, classification, details):
    try:
        user = User.objects.get(pk=user_id)
        friend = Friend.objects.get(pk=friend_id)
        event = Event(name=name, date=date, user=user, friend = friend, classification= classification, details=details)
        event.full_clean()
        event.save()
        return event
    except User.DoesNotExist:
        print(f'User {user_id} does not exist')
        return None
    except Friend.DoesNotExist:
        print(f'Friend {friend_id} does not exist')
        return None
    except Exception as e:
        print(f'Exception when saving event: {e}')
        return None

# Modify event with all attributes
def edit_event_details(event_id, field_values):
    # field_values: dictionary containing values to update
    try:
        event = Event.objects.get(pk=event_id)
        for field, value in field_values.items():
            if hasattr(event, field):
                setattr(event, field, value)
        event.full_clean()
        event.save()
        return True
    except Event.DoesNotExist:
        print(f'Event {event_id} does not exist')
        return False
    except Exception as e:
        print(f'Exception when editing event: {e}')
        return False

# Read the event details
def read_event_details(event_id):
    try:
        event = Event.objects.get(pk=event_id)
        return event
    except Event.DoesNotExist:
        print(f'Event {event_id} does not exist')
        return None
    except Exception as e:
        print(f'Exception when reading event: {e}')
        return None

# Delete the event
def delete_event(event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
        return True
    except Event.DoesNotExist:
        print(f'Event {event_id} does not exist')
        return False
    except Exception as e:
        print(f'Exception when deleting event: {e}')
        return False

# Group and order event based on provided month
def group_event_by_month(user_id, month):
    # month is provided in 'MM/YYYY' string format
    try:
        parsed_date = datetime.strptime(month, "%m/%Y")
        month_num = parsed_date.month
        year_num = parsed_date.year

        # Filter events by the extracted month and year
        filtered_events = Event.objects.filter(user_id = user_id,date__month=month_num, date__year=year_num).order_by('date')
        return filtered_events
    except Exception as e:
        print(f'Exception when grouping event in a month: {e}')
        return None

# Group and order event based on provided day
def group_event_by_day(user_id, day):
    # day is provided in 'DD/MM/YYYY' string format
    try:
        # Parse the day, month, and year from the input string
        parsed_date = datetime.strptime(day, "%d/%m/%Y")
        filtered_events = Event.objects.filter(user_id = user_id, date=parsed_date.date()).order_by('date')
        return filtered_events
    except Exception as e:
        print(f'Exception when grouping event on a specific day: {e}')
        return None

# Get event list from a friend
def get_friend_event_list(friend_id):
    try:
        event_list = Event.objects.filter(friend_id = friend_id)
        return event_list
    except Exception as e:
        print(f'Exception when getting friend event list: {e}')
        return None

# Get event list for user:
def get_user_event_list(user_id):
    try:
        event_list = Event.objects.filter(user_id=user_id)
        return event_list
    except Exception as e:
        print(f'Exception when getting user event list: {e}')
        return None


