from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'No-op: sample project illustrations are disabled for real portfolio projects.'

    def handle(self, *args, **options):
        self.stdout.write('Skipped: sample illustrations disabled')

