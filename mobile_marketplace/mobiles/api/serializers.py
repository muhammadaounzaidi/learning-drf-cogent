from rest_framework import serializers
from mobile_marketplace.mobiles.models import Mobile


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = (
            'id',
            'name',
            'company',
            'description',
            'is_sold',
            'condition',
            'user',
            'sold_amount'
            )
