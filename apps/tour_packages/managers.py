from django.db.models import Manager
from .choices import PackageDisplayChoices


class TourPackageManager(Manager):
    def main_banner(self):
        return self.filter(package_type=PackageDisplayChoices.MAIN_BANNER)

    def regular(self):
        return self.filter(package_type=PackageDisplayChoices.REGULAR)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
