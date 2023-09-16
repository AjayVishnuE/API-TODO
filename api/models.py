from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password =models.CharField(max_length=255)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=100, blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
