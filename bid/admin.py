from django.contrib import admin
from bid.models import Bid


# Register your models here.

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('bid_amount','mobile','user')
