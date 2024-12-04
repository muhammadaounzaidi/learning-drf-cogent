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

    def has_valid_bid(self):
        bid = Bid.objects.filter(mobile=self.mobile).last()
        return bid is not None and bid.amount > 0

    @transition(field=state, source=BidStateTypes.PENDING, target=BidStateTypes.ACCEPTED, conditions=[has_valid_bid])
    def accept_bid(self):
        if self.has_valid_bid():
            self.mobile.is_sold = True
            self.mobile.save()

            Bid.objects.filter(mobile=self.mobile).exclude(id=self.id).update(state=BidStateTypes.REJECTED)

            self.state = BidStateTypes.ACCEPTED
            self.save()
            return self
        return None


    def __str__(self):
        return str(self.amount)
