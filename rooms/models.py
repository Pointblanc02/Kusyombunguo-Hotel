from django.db import models

# Create your models here.

class Room(models.Model):
    arrival = models.IntegerField(blank=False)
    departure = models.IntegerField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    guests = models.IntegerField(blank=False)
