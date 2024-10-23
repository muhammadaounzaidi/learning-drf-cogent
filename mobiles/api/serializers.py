from rest_framework import serializers
from mobiles.models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('name','company', 'description', 'condition','user')
