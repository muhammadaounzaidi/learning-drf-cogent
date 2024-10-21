from django.db import models

from mobile.models import Mobile
from user.models import User

from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Bid(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    mobile=models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='bids')
    bid_amount = models.IntegerField()
    is_sold = models.BooleanField(default=False)