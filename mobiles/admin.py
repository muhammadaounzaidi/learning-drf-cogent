# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Mobile


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
        'user',
    )
    list_filter = ('created', 'modified', 'user')
