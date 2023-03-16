from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(ClubUser)
class UserInAdmin(UserAdmin):
    """ All User Admin Model (Include Super User) """
    # The forms to add and change user instances
    search_fields = ['username',
                     'first_name',
                     'last_name',
                     'is_superuser',
                     'is_staff',
                     'is_active']
    list_display = ['username', 'is_superuser', 'is_staff', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    fieldsets = (
        (None, {'fields': ('username',
                           'password', ('first_name', 'last_name'),)}),
        ('Contact', {
            # 'classes': ('collapse',),
            'fields': (('phone_number', 'email'),)
        }),
        ('Biographical Details', {
            # 'classes': ('collapse',),
            'fields': ('avatar',)
        }),
        ('Permissions',
         {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Time', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ('first_name',
                       'last_name',
                       'username',
                       'password1',
                       'password2')}
         ),
    )
    ordering = ('username',)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(LogEntry)
