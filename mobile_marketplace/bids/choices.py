from django.db import models


class BidStateTypes(models.TextChoices):
    PENDING = "PENDING", "pending"
    REJECTED = "REJECTED", "rejected"
    ACCEPTED = "ACCEPTED", "accepted"
