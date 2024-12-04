from mobile_marketplace.bids.models import Bid


def has_valid_bid(self):
    bid = Bid.objects.filter(mobile=self.mobile).last()
    return bid is not None and bid.amount > 0