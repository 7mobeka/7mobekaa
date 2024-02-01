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
    path('user_messages/', user_messages, name='user_messages'),
    path('create-appointment/<str:volunteer_username>/<str:senior_citizen_username>/', create_appointment, name='create_appointment'),
    path('view-appointment/', view_appointment, name='view_appointment'),
    path('edit-appointment/', edit_appointment, name='edit_appointment'),
    # ... other urlpatterns ...
 ]