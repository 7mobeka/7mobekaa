
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'first_name', 'last_name', 'email', 'type', 'phone_number', 'bio']
class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']