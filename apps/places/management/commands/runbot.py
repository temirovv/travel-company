from django.core.management.base import BaseCommand
from apps.places.bot.app import run


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        run()
