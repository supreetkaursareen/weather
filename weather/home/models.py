# models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username
