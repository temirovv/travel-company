from django.core.management.base import BaseCommand
from apps.utils.bot.main import run


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        run()
