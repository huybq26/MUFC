# serializers.py
from rest_framework import serializers

from .model.event import Event
from .model.hobby import Hobby
from .model.user import User
from .model.friend import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = [
            'friend_id',
            'user_id',
            'name',
            'email',
            'phone',
            'dob',
            'level_friendship',
            'last_contacted',
            'notes',
            'facebook',
            'whatsapp',
            'insta',
            'tele',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'name',
            'email',
            'phone',
            'password',
            'dob',
            'tele',
        ]

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = [
            'hobby_id',
            'name',
            'notes',
        ]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_id',
            'name',
            'date',
            'user',
            'friend',
            'classification',
            'details',
        ]



