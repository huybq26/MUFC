import uuid
from django.db import models

from model.person import Person


class User (Person):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

