from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('user_list/', user_list, name='user_list'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
     path('events/', event_list, name='event_list'),
     path('apply/<int:event_id>/<slug:event_name>/', apply_for_event, name='apply_for_event'),
    
    path('send_message/<str:recipient>/', send_message, name='send_message_with_recipient'),
     path('inbox/', inbox, name='inbox'),
     path('sent_messages/', sent_messages, name='sent_messages'),

     path('user_messages/', user_messages, name='user_messages')
]
