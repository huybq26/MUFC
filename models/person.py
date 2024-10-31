import uuid
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    dob = models.DateField()
    tele = models.CharField(max_length=50)

    class Meta:
        abstract = True