from django.db import models
from user.models import User
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Mobile(TimeStampedModel):
    MOBILE_CONDITION_CHOICES = [
        ('refurbished', 'Refurbished'),
        ('new', 'New'),
        ('old', 'Old'),
    ]
    mobile_name=models.CharField(max_length=255)
    mobile_company=models.CharField(max_length=255)
    mobile_description=models.TextField()
    mobile_condition=models.CharField(max_length=20,choices=MOBILE_CONDITION_CHOICES)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name = "mobile" )
    def __str__(self):
        return self.mobile_name
