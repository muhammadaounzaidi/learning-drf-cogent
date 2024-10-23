from django.db import models

from mobiles.models import Mobile
from users.models import User

from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Bid(TimeStampedModel):
    amount = models.IntegerField()
    is_sold = models.BooleanField(default=False)

    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')

    def __str__(self):
        return self.amount
