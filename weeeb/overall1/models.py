# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)  
    VOLUNTEER = 'volunteer'
    CITIZEN = 'citizen'
    USER_TYPES = [
        (VOLUNTEER, 'Volunteer'),
        (CITIZEN, 'Citizen'),
    ]
    type = models.CharField(max_length=20, choices=USER_TYPES, blank=True, null=True)
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    counter = models.IntegerField(default=0)

    

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)


STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
]

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    senior_citizen = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='senior_citizen_appointments', null=True, blank=True)
    volunteer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='volunteer_appointments', null=True, blank=True)
    senior_citizen_message = models.TextField()
    volunteer_message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)