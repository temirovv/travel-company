from django.db.models import TextChoices


class PackageDisplayChoices(TextChoices):
    MAIN_BANNER = 'main_banner', 'Main Banner'
    REGULAR = 'regular', 'Regular'
