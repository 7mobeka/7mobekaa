# overall/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('volunteers/', DisplayUsersListView.as_view(), name='volunteers'),
    path('aboutus/', aboutus, name='aboutus'),
    path('events/', display_events, name='events'),
    path('coverdview/', some_protected_view, name='coverdview'),



    path('register/', register, name='register'),  # Corrected the reference to the view function
    path('login/', login_view, name='login'), 


    path('create_event/', create_event, name='create_event'),
    path('failed/', failed, name='failed'),
]