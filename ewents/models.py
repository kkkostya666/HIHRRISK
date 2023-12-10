from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Events(models.Model):
    id = models.IntegerField(unique=True)
    name_events = models.CharField(max_length=100)
    description_events = models.CharField(max_length=250, blank=True)




