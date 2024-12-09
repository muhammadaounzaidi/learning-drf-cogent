import logging
from django.utils import timezone
from datetime import timedelta
from mobile_marketplace.mobiles.models import Mobile
from celery import shared_task

logger = logging.getLogger('mobile_marketplace')


@shared_task
def deleting_mobiles_after_14_days():
    mobiles_to_delete = Mobile.objects.filter(created__lt=timezone.now() - timedelta(days=14))
    deleted_count, _ = mobiles_to_delete.delete()

    if deleted_count:
        logger.info(f'{deleted_count} mobile objects deleted successfully.')
    else:
        logger.info('No objects to delete.')