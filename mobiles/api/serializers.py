from rest_framework import serializers
from mobiles.models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('mobile_name','mobile_company','mobile_description','mobile_condition','user')
