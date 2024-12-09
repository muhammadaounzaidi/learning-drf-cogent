from django.utils import timezone
from datetime import timedelta
from mobile_marketplace.mobiles.models import Mobile
from celery import shared_task


@shared_task
def deleting_mobiles_after_14_days():
    fourteen_days_ago = timezone.now() - timedelta(days=14)
    mobiles_to_delete = Mobile.objects.filter(created__lt=fourteen_days_ago)
    deleted_count, _ = mobiles_to_delete.delete()
    
    if deleted_count:
        print(f'{deleted_count} mobile objects deleted successfully.')
    else:
        print('No objects to delete.')
