from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Participant

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'name', 'ramal', 'is_administrator',
                       'is_participant', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'name', 'ramal','is_administrator', 'is_participant', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_administrator', 'is_participant']
    search_fields = ('email', 'username')
    ordering = ('username',)


admin.site.register(Participant)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)