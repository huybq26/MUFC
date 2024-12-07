import uuid
from django.db import models

from MUFC2.model.person import Person


class User (Person):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, verbose_name="Username")
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

