m
from django.core.management.base import BaseCommand
from django.utils import timezone

from subscriptions.models import Subscription


class Command(BaseCommand):

    help = "Subscription statuslarini yangilaydi"

    def handle(self, *args, **kwargs):

        expired_subscriptions = Subscription.objects.filter(
            status='active',
            end_date__lt=timezone.now()
        )

        updated_count = expired_subscriptions.update(
            status='expired'
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{updated_count} ta subscription expired qilindi"
            )
        )

