from rest_framework import serializers
from mobile_marketplace.bids.models import Bid


class BidSerializer(serializers.ModelSerializer):
    # status = serializers.CharField(max_length=255, default='PENDING', required=False)

    class Meta:
        model = Bid
        fields = (
            'amount',
            'user',
            'mobile',
            'status'
            )
