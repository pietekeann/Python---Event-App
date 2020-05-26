from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Facility, Event

admin.site.register(Facility)

admin.site.register(Event)