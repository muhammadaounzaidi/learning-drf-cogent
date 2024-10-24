from rest_framework import serializers
from bids.models import Bid


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['amount', 'is_last_bid', 'user', 'mobile']
