import uuid
from django.db import models

from model.friend import Friend
from model.user import User


class Hobby(models.Model):
    hobby_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.name  # Return the name of the hobby

