from django.contrib import admin

# Register your models here.
from .models import Room

#Create authentication and authorization
admin.site.register(Room)