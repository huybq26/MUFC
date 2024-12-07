import uuid
from django.db import models

from MUFC2.model.friend import Friend
from MUFC2.model.user import User


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    classification = models.BooleanField(default=False)
    details = models.TextField()

    def __str__(self):
        return self.name  # Return the event name

