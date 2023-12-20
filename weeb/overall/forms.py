# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile , Event , UserEventApplication
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect  


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['type', 'image', 'description', 'age', 'address', 'phone_number']

    
class CustomRegistrationForm(UserCreationForm):#registration and creat user account
    TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('senior_citizen', 'Senior Citizen'),
    ]
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'type']


class UsersDisplayForm(forms.ModelForm): #Display users
    class Meta:
        model = UserProfile
        fields = ['userid','user', 'type', 'image', 'description', 'age', 'address', 'phone_number']



class EventForm(forms.ModelForm):#admin creat event
    class Meta:
        model = Event
        fields = ['name', 'image', 'description', 'address', 'start_date', 'end_date']



class UserEventApplicationForm(forms.ModelForm): #users apply to events ceated
    class Meta:
        model = UserEventApplication
        fields = ['user_name', 'user_email', 'event']



class LoginForm(AuthenticationForm):#login view 
    pass