from django.contrib import admin
from bids.models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'amount',
        'is_last_bid',
    )
    list_filter = ('created', 'modified', 'is_last_bid')
