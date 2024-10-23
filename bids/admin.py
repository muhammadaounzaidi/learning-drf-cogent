# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'mobile',
        'bid_amount',
        'is_sold',
    )
    list_filter = ('created', 'modified', 'user', 'mobile', 'is_sold')
