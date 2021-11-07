import os

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Init seeding database'

    def handle(self, *args, **options):
        sapp = SocialApp(
            provider='github', name='Github',
            client_id=os.environ.get('GITHUB_CLIENT_ID'),
            secret=os.environ.get('GITHUB_SECRET')
        )
        sapp.save()
        sapp.sites.add(1)
