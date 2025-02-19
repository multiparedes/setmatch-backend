from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

class UserChoices(models.Choices):
    ADMIN = 'Admin'
    USER = 'User'
    Trainer = 'Trainer'

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.CharField(max_length=50, choices=UserChoices, default=UserChoices.USER)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username