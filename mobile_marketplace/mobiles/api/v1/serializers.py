from rest_framework import serializers
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.users.models import User
from mobile_marketplace.bids.choices import BidStateTypes
from mobile_marketplace.bids.api.v1.serializers import BidSerializer


class MobileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.filter(is_active=True),
    )
    pending_bids_count = serializers.IntegerField(read_only=True)
    pending_bids = serializers.SerializerMethodField()

    class Meta:
        model = Mobile
        fields = (
            'id',
            'name',
            'company',
            'description',
            'is_sold',
            'condition',
            'asking_amount',
            'user',
            'pending_bids_count',
            'pending_bids',
        )

    def get_pending_bids(self, obj):
        pending_bids = obj.bids.filter(state=BidStateTypes.PENDING)
        return BidSerializer(pending_bids, many=True).data
