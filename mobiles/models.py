from django.db import models
from users.models import User
from django_extensions.db.models import TimeStampedModel
from mobiles.choices import MOBILE_CONDITION_CHOICES


class Mobile(TimeStampedModel):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=20, choices=MOBILE_CONDITION_CHOICES)
    is_sold = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mobiles")

    def __str__(self):
        return self.name
