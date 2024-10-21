from django.contrib import admin
from mobiles.models import Mobile
# Register your models here.

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('mobile_name','mobile_company','mobile_description','mobile_condition')
