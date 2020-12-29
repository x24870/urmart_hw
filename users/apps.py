
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import AppConfig

from .models import User

class UserConfig(AppConfig):
    name = 'users'

admin.site.register(User, UserAdmin)