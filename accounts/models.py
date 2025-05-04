from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser) :
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('starter', 'Starter'),
        ('pro', 'Pro'),
        ('premium', 'Premium'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    plan = models.CharField(max_length=30, choices=PLAN_CHOICES, default='free')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email