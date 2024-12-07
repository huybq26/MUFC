import uuid

from django.db import models

from MUFC2.model.friend import Friend


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(Friend, related_name="friend_tags")

    def __str__(self):
        return self.name