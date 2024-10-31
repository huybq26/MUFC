import uuid
from django.db import models

from model.friend import Friend
from model.user import User


class Hobby(models.Model):
    hobby_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    users = models.ManyToManyField(User, related_name="user_hobbies")  # Unique related_name
    friends = models.ManyToManyField(Friend, related_name="friend_hobbies")  # Unique related_name

    def __str__(self):
        return self.name  # Return the name of the hobby

