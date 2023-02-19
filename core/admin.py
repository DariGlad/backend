from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
    )
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined',)
    add_fieldsets = (
        (None,
         {"fields": (
             "username",
             "password1",
             "password2"
         )}),
        ('Персональная информация',
         {"fields": (
             "first_name",
             "last_name",
             "email",
         )}),
        ('Права доступа',
         {"fields": (
             "is_staff",
         )}),
    )
