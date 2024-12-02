from django.db import models
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.users.models import User
from django_extensions.db.models import TimeStampedModel
from mobile_marketplace.bids.choices import BidStateTypes


class Bid(TimeStampedModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=BidStateTypes, default="PENDING")

    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')

    def __str__(self):
        return str(self.amount)
