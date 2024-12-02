from rest_framework import serializers
from mobile_marketplace.bids.models import Bid


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = (
            'amount',
            'user',
            'mobile',
            'status'
            )
