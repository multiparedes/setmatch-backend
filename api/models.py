from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import uuid

class UserChoices(models.TextChoices):
    ADMIN = 'Admin'
    USER = 'User'
    TRAINER = 'Trainer'

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

class Schedule(models.Model):
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return f'From {self.start_hour} to {self.end_hour}'

class Location(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Court(models.Model):
    class CourtChoices(models.TextChoices):
        DIRT = 'Dirt'
        GRASS = 'Grass'
        CLAY = 'Clay'
        CONCRETE = 'Concrete'

    surface_type = models.CharField(choices=CourtChoices, max_length=25, default=CourtChoices.CONCRETE)
    max_players = models.PositiveIntegerField()
    court_price = models.PositiveIntegerField()

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'Court of {self.surface_type} for {self.max_players} players'

class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Trainer'}, null=True, related_name='trainer')
    participants = models.ManyToManyField(User, limit_choices_to={'role': 'User'}, related_name='participants')

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_paid = models.BooleanField(default=False)

    def pay_reservation(self):
        self.is_paid = True
        self.save()

    def __str__(self):
        return f"Reservation {self.id}: {'Not' if not self.is_paid else ''}paid"
