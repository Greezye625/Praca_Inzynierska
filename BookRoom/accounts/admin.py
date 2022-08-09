from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.TabularInline):
    model = UserProfile


class UserWithProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserWithProfileAdmin)


