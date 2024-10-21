from django.contrib import admin
from bids.models import Bid


# Register your models here.

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('bid_amount',)
