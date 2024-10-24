from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'created',
        'modified',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'created',
        'modified',
    )
    raw_id_fields = ('groups', 'user_permissions')
