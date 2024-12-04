from django.db import models


class BidStateTypes(models.TextChoices):
    PENDING = "PENDING", "Pending"
    REJECTED = "REJECTED", "Rejected"
    ACCEPTED = "ACCEPTED", "Accepted"
