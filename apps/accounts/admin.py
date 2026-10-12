from django.contrib import admin
# 1. Import the built-in UserAdmin class
from django.contrib.auth.admin import UserAdmin 
from .models import User

# 2. Register your custom User model using the inherited UserAdmin settings
admin.site.register(User, UserAdmin)
