from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_fname', 'user_lname', 'user_email', 'user_position']

admin.site.register(User, UserAdmin)

