from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


class User(models.Model):
    user_fname = models.CharField(max_length=200, verbose_name='First Name')
    user_lname = models.CharField(max_length=200, verbose_name='Last Name')
    user_email = models.EmailField(unique=True, max_length=200, verbose_name='Email')
    user_position = models.CharField(max_length=200, verbose_name='First Name')
    pub_date = models.DateField(default=now)
    def __str__(self):
        return self.user_email

