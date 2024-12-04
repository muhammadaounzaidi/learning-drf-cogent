from rest_framework import serializers
from mobile_marketplace.bids.models import Bid
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.users.models import User


class BidSerializer(serializers.ModelSerializer):
    mobile = serializers.PrimaryKeyRelatedField(queryset=Mobile.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.filter(is_active=True),
    )

    class Meta:
        model = Bid
        fields = (
            'id',
            'amount',
            'mobile',
            'state',
            'user'
            )
