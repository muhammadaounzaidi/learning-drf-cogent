from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from mobile_marketplace.mobiles.models import Mobile


class Command(BaseCommand):
    help = "Delete Mobile objects older than 14 days."

    def handle(self, *args, **options):
        fourteen_days_ago = timezone.now() - timedelta(days=14)
        mobiles_to_delete = Mobile.objects.filter(created__lt=fourteen_days_ago)
        deleted_count, _ = mobiles_to_delete.delete()

        if deleted_count:
            self.stdout.write(self.style.SUCCESS(f'{deleted_count} mobile objects deleted successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('No objects to delete.'))
