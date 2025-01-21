from django.contrib import admin
from mobile_marketplace.mobiles.models import Mobile


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
        'asking_amount',
    )
    list_filter = ('created', 'modified')
