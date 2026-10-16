import os
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.core.management import call_command, CommandError
from django.test import TestCase

class BootstrapTests(TestCase):
    credentials = {'DJANGO_SUPERUSER_USERNAME':'owner','DJANGO_SUPERUSER_EMAIL':'owner@example.com','DJANGO_SUPERUSER_PASSWORD':'A-long-test-only-passphrase-723!'}

    def test_create_once_without_resetting_password(self):
        with patch.dict(os.environ,self.credentials):
            call_command('bootstrap_admin')
        user=get_user_model().objects.get(username='owner')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(self.credentials['DJANGO_SUPERUSER_PASSWORD']))
        original=user.password
        with patch.dict(os.environ,{'DJANGO_SUPERUSER_PASSWORD':'different'}):
            call_command('bootstrap_admin')
        user.refresh_from_db()
        self.assertEqual(user.password,original)
        self.assertEqual(get_user_model().objects.count(),1)

    def test_requires_credentials(self):
        with patch.dict(os.environ,{k:'' for k in self.credentials}):
            with self.assertRaises(CommandError):call_command('bootstrap_admin')

    def test_does_not_promote_existing_user(self):
        get_user_model().objects.create_user(username='owner')
        with patch.dict(os.environ,self.credentials):
            with self.assertRaises(CommandError):call_command('bootstrap_admin')
        self.assertFalse(get_user_model().objects.get().is_superuser)

    def test_rejects_weak_password(self):
        with patch.dict(os.environ,{**self.credentials,'DJANGO_SUPERUSER_PASSWORD':'123'}):
            with self.assertRaises(CommandError):call_command('bootstrap_admin')
        self.assertFalse(get_user_model().objects.exists())
