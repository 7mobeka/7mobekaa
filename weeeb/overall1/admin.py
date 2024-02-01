# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Apply)
admin.site.register(Message)

admin.site.register(Appointment)