# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomRegistrationForm(UserCreationForm):
    TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('senior_citizen', 'Senior Citizen'),
    ]
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'type']

class UsersDisplayForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'type', 'image', 'description', 'age', 'address', 'phone_number']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'start_date', 'end_date']
