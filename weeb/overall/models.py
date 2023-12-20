# models.py
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.AutoField(primary_key=True, unique=True)
    TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('senior_citizen', 'Senior Citizen'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)
    
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
     if created:
        UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
     instance.userprofile.save()


class Event(models.Model):
    name = models.CharField(max_length=255,null=True)
    application_count = models.IntegerField(default=0)  
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name


class UserEventApplication(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} - {self.event.name}"
    
    