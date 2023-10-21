import datetime
from django.core.management.base import BaseCommand
from email_distribution.scheduler import send_email


class Command(BaseCommand):
    help = 'Send scheduled email'

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        self.stdout.write(f'Sending scheduled email at {now}')
        send_email()

        self.stdout.write(self.style.SUCCESS('Scheduled email sent successfully'))