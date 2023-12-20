# overall/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('home/', home, name='home'),
    path('volunteers/', DisplayUsersListView.as_view(), name='volunteers'),
    path('aboutus/', aboutus, name='aboutus'),
    path('events/', display_events, name='events'),
    path('coverdview/', some_protected_view, name='coverdview'),
    path('apply_event/', apply_event, name='apply_event'),


    path('register/', register, name='register'),  # Corrected the reference to the view function
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_button, name='logout_button'),

    path('create_event/', create_event, name='create_event'),
    path('failed/', failed, name='failed'),

    path('view_profile/', view_profile, name='view_profile'),
    path('display_application/', display_application, name='display_application'),
    path('all_users/', all_users, name='all_users'),

    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
