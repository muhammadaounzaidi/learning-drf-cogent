from django.contrib import admin
from mobiles.models import Mobile


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'name',
        'company',
        'description',
        'condition',
        'is_sold',
    )
    list_filter = ('created', 'modified')
