from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.exceptions import PermissionDenied




def home(request):
    return render(request, 'overall1/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            
            UserProfile.objects.create(user=user)

            return redirect('login_user')
    else:
        form = UserCreationForm()

    return render(request, 'overall1/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'overall1/login_user.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def view_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'overall1/view_profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'overall1/edit_profile.html', {'form': form})


@login_required
def user_list(request):
    volunteer_users = UserProfile.objects.filter(type='volunteer').select_related('user')

    return render(request, 'overall1/user_list.html', {'users': volunteer_users})

def event_list(request):
    all_events = Event.objects.all()

    return render(request, 'overall1/event_list.html', {'events': all_events})

@login_required
def apply_for_event(request, event_id, event_name):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        Apply.objects.create(user=request.user, event=event)
        event.counter += 1
        event.save()
        return redirect('event_list')

    return render(request, 'overall1/apply_for_event.html', {'event': event, 'event_name': event_name})




def send_message(request, recipient):
    try:
        recipient_user = User.objects.get(username=recipient)
    except User.DoesNotExist:
        return redirect('user_list')

    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient_user
            message.save()
            return redirect('user_messages')
    else:
        form = SendMessageForm(initial={'recipient': recipient_user.pk})

    return render(request, 'overall1/send_message.html', {'form': form, 'recipient': recipient_user})


@login_required
def user_messages(request):
    sent_messages = Message.objects.filter(sender=request.user)
    received_messages = Message.objects.filter(recipient=request.user)

    return render(request, 'overall1/user_messages.html', {
        'sent_messages': sent_messages,
        'received_messages': received_messages
    })

@login_required
def create_appointment(request, volunteer_username, senior_citizen_username):
    if request.method == 'POST':
        form = SeniorCitizenMessageForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.volunteer_username = volunteer_username
            appointment.senior_citizen_username = senior_citizen_username
            appointment.status = 'pending'  
            appointment.save()
            return redirect('view_appointment')
    else:
        form = SeniorCitizenMessageForm()

    return render(request, 'overall1/create_appointment.html', {'form': form})


@login_required
def view_appointment(request):
    
    appointments = Appointment.objects.filter(
        Q(senior_citizen_username=request.user.username) | 
        Q(volunteer_username=request.user.username)
    )

    return render(request, 'overall1/view_appointment.html', {'appointments': appointments})

def edit_appointment(request):
    # Fetch appointments where the current user is the volunteer
    appointments = Appointment.objects.filter(
        volunteer_username=request.user.username,
        status='pending'  # Or whatever status you want to filter
    )

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id, volunteer_username=request.user.username)
        form = VolunteerMessageForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('view_appointment')  # Redirect to the user list or any other appropriate page
    else:
        form = VolunteerMessageForm()

    return render(request, 'overall1/edit_appointment.html', {'appointments': appointments, 'form': form})
