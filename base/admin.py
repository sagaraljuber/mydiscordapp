from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

#Create authentication and authorization
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)