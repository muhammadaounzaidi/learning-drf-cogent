from rest_framework import serializers
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.users.models import User


class MobileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.filter(is_active=True),
    )
    pending_bids_count = serializers.IntegerField(read_only=True)

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
            )
