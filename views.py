from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Additional logic if needed
            user_type = form.cleaned_data['type']

            # Check if UserProfile exists, create if not
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            # Save the 'type' field to UserProfile
            user_profile.type = user_type
            user_profile.save()

            # Log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            # Redirect to the desired URL after successful registration
            return redirect('coverdview')  # Change 'coverdview' to your desired URL
    else:
        form = CustomRegistrationForm()

    return render(request, 'overall/register.html', {'form': form})

class DisplayUsersListView(ListView):
    model = UserProfile
    template_name = 'overall/volunteers.html'
    context_object_name = 'user_profiles'

def home(request):
    return render(request, 'overall/home.html')

def display_events(request):
    events = Event.objects.all()
    return render(request, 'overall/events.html', {'events': events})

def failed(request):
    return render(request, 'overall/failed.html')


def aboutus(request):
    return render(request, 'overall/aboutus.html')

def some_protected_view(request):
    return render(request, 'overall/coverdview.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        # Your authentication logic
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Successful login, you can redirect to a specific page
            return redirect('coverdview')
        else:
            # Unsuccessful login, handle accordingly
            return render(request, 'overall/failed.html')

    return render(request, 'overall/login.html')




def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            
            event.save()
            return redirect('coverdview')  # Redirect to the coverdview page if successful
        else:
            return redirect('failed')  # Redirect to the failed page if form is not valid
    else:
        form = EventForm()

    return render(request, 'overall/create_event.html', {'form': form})

