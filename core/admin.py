from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from core.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'company_link'
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
             "company"
         )}),
        ('Права доступа',
         {"fields": (
             "is_staff",
         )}),
    )
    fieldsets = (
        (None,
         {"fields": (
             "username",
             "password",
         )}),
        ('Персональная информация',
         {"fields": (
             "first_name",
             "last_name",
             "email",
             "company"
         )}),
        ('Права доступа',
         {"fields": (
             "is_staff",
             "is_active",
             "groups",
             "user_permissions"
         )}),
    )

    @admin.display(description='Компания')
    def company_link(self, obj):
        if obj.company:
            link = reverse(
                'admin:company_company_change',
                args=(obj.company.id,)
            )
            return mark_safe(u'<a href="{0}">{1}</a>'.format(link, obj.company))
