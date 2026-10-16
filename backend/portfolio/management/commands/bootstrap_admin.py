import os

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create the first admin from environment variables without changing existing accounts.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', '').strip()
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '').strip()
        if User.objects.filter(is_superuser=True, is_active=True).exists():
            self.stdout.write('Admin already exists; credentials unchanged.')
            return
        if not all([username, password, email]):
            raise CommandError('Set DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD on Render.')
        if User.objects.filter(username=username).exists():
            raise CommandError('Username already exists; choose another username. Existing users are never promoted.')
        try:
            validate_password(password, User(username=username, email=email))
        except ValidationError:
            raise CommandError('Admin password does not meet Django password requirements.') from None
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Admin created. Remove bootstrap credentials from Render Environment.'))
