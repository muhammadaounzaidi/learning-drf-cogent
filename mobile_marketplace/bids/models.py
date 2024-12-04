from django.db import models
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.users.models import User
from django_extensions.db.models import TimeStampedModel
from mobile_marketplace.bids.choices import BidStateTypes
from django_fsm import FSMField, transition


class Bid(TimeStampedModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = FSMField(default=BidStateTypes.PENDING, choices=BidStateTypes)

    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

    @transition(field=state, source=BidStateTypes.PENDING, target=BidStateTypes.ACCEPTED)
    def accept_bid(self):
        self.mobile.is_sold = True
        self.mobile.save(update_fields=['is_sold'])

        Bid.objects.filter(mobile=self.mobile).exclude(id=self.id).update(state=BidStateTypes.REJECTED)

        self.state = BidStateTypes.ACCEPTED
        self.save()

    def __str__(self):
        return str(self.amount)
