from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)
    image = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    type = forms.ChoiceField(choices=UserProfile.USER_TYPES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'bio', 'first_name', 'last_name', 'email', 'image', 'phone_number', 'type']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user_profile = UserProfile(
            user=user,
            bio=self.cleaned_data['bio'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            image=self.cleaned_data['image'],
            phone_number=self.cleaned_data['phone_number'],
            type=self.cleaned_data['type']
        )

        if commit:
            user.save()
            user_profile.save()

        return user
    
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'first_name', 'last_name', 'email', 'type', 'phone_number', 'bio']


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']

class SeniorCitizenMessageForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['senior_citizen_message']

class VolunteerAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['volunteer_message', 'status']

class VolunteerMessageForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['volunteer_message', 'status']