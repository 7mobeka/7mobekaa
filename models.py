# models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('senior_citizen', 'Senior Citizen'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)
    
    # Additional fields
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='event_images/', null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_created',null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name