from django.db import models
from mobile_marketplace.users.models import User
from django_extensions.db.models import TimeStampedModel
from mobile_marketplace.mobiles.choices import MobileConditionType


class Mobile(TimeStampedModel):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=255, choices=MobileConditionType)
    is_sold = models.BooleanField(default=False)
    asking_amount = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mobiles")

    def __str__(self):
        return self.name
