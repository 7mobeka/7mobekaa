

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth import logout





def logout_button(request):
    logout(request)
    return redirect('home')  # Redirect to your desired page after logout


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
    context_object_name = 'volunteers'

    def get_queryset(self):
        # Filter users based on the type 'volunteer'
        return UserProfile.objects.filter(type='volunteer')

def home(request):
    return render(request, 'overall/home.html')

def display_events(request):
    events = Event.objects.all()
    return render(request, 'overall/events.html', {'events': events})

def display_application(request):
    applications = UserEventApplication.objects.all()
    return render(request, 'overall/display_application.html', {'display_application': applications})

def failed(request):
    return render(request, 'overall/failed.html')


def aboutus(request):
    return render(request, 'overall/aboutus.html')

def some_protected_view(request):
    return render(request, 'overall/coverdview.html')



class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'overall/login.html'

    def form_valid(self, form):
        # Perform the default login logic
        response = super().form_valid(form)

        # Redirect to coverdview.html upon successful login
        return redirect('view_profile')

    def form_invalid(self, form):
        # Perform the default login error logic
        response = super().form_invalid(form)

        # Redirect to failed.html upon unsuccessful login
        return redirect('failed')


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('coverdview')  # Redirect to the coverdview page if successful
        else:
            return redirect('failed')  # Redirect to the failed page if form is not valid
    else:
        form = EventForm()

    return render(request, 'overall/create_event.html', {'form': form})



def apply_event(request):
   if request.method == 'POST':
        form = UserEventApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()

            # Increment the counter for the chosen event
            event_id = request.POST.get('event')
            if event_id:
                event = get_object_or_404(Event, id=event_id)
                event.application_count += 1
                event.save()

            return redirect('coverdview')  # Redirect to the coverdview page if successful
   else:
        form = UserEventApplicationForm()

    # If the form is not valid, render the template with the form and display validation errors
   return render(request, 'overall/apply_event.html', {'form': form})

@login_required(login_url='/login/')
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'overall/view_profile.html', {'form': form, 'username': request.user.username})


def all_users(request):
    users = User.objects.all()
    return render(request, 'overall/all_users.html', {'users': users})