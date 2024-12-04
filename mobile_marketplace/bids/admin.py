from django.contrib import admin
from mobile_marketplace.bids.models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'amount',
        'state',
    )
    list_filter = ('created', 'modified')
