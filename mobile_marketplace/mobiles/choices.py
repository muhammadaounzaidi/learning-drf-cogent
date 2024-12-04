from django.db import models


class MobileConditionType(models.TextChoices):
    REFURBISHED = "REFURBISHED", "Refurbished"
    NEW = "NEW", "New"
    OLD = "OLD", "Old"

