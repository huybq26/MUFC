import uuid
from django.db import models

from MUFC2.model.hobby import Hobby
from MUFC2.model.person import Person
from MUFC2.model.user import User


class Friend(Person):
    friend_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    level_friendship = models.IntegerField(default=0)
    last_contacted = models.DateTimeField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    facebook = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    insta = models.CharField(max_length=50)
    hobbies = models.ManyToManyField(Hobby, related_name="friends")

    def __str__(self):
        return self.name


