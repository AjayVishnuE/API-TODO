from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255 , unique=True)
    email = models.CharField(max_length=255, unique=True)
    password =models.CharField(max_length=255)

    first_name = None
    last_name = None
    name = None

class ToDo(models.Model):
    # user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    Title = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=100, blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
