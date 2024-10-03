# tours/py
from django.contrib.auth import get_user_model
from django.db.models import CharField, TextField, DecimalField, PositiveIntegerField, DateField, ManyToManyField, \
    DateTimeField, ImageField, Model, ForeignKey, CASCADE, TimeField, BooleanField, SlugField
from django.utils.text import slugify

from .choices import PackageDisplayChoices
from .managers import TourPackageManager


class Destination(Model):
    name = CharField(max_length=255, help_text="Manzilning nomi (shahar yoki diqqatga sazovor joy)") # noqa
    description = TextField(blank=True, help_text="Manzil haqida qisqacha ma'lumot") # noqa
    country = CharField(max_length=100, help_text="Mamlakat") # noqa
    city = CharField(max_length=100, help_text="Shahar") # noqa
    attractions = TextField(blank=True, help_text="Diqqatga sazovor joylar") # noqa
    gallery = ManyToManyField(
        'Gallery', through='DestinationGallery',
        related_name='destinations', help_text="Manzilga tegishli rasmlar") # noqa
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True, blank=True, null=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while TourPackage.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.name}, {self.city}"


class TourPackage(Model):
    title = CharField(max_length=255)
    description = TextField(help_text="A detailed description of the tour package")
    price = DecimalField(max_digits=10, decimal_places=2)
    duration = PositiveIntegerField(help_text="Duration in days")
    start_date = DateField()
    end_date = DateField()
    group_size = PositiveIntegerField(help_text="Number of people in the group")
    languages_offered = CharField(max_length=255, help_text="Languages available for the tour")
    destinations = ManyToManyField(
        'Destination', through='TourPackageDestination',
        related_name='tour_packages', help_text="Sayohatdagi manzillar") # noqa
    rating = DecimalField(max_digits=3, decimal_places=2, default=4.5)
    review_count = PositiveIntegerField(default=0)
    gallery = ManyToManyField('Gallery', through='TourPackageGallery', related_name='tour_packages')
    created_at = DateTimeField(auto_now_add=True)
    package_type = CharField(max_length=15, choices=PackageDisplayChoices.choices,
                             default=PackageDisplayChoices.REGULAR)
    is_active = BooleanField(default=True)
    slug = SlugField(max_length=255, unique=True, blank=True, null=True)

    objects = TourPackageManager()

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while TourPackage.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class Gallery(Model):
    title = CharField(max_length=255, blank=True, null=True, help_text="Rasmning nomi") # noqa
    image = ImageField(upload_to='gallery/')
    description = CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Galeriya' # noqa
        verbose_name_plural = 'Galeriya' # noqa
        ordering = ['-id']

    def __str__(self):
        return f"Gallery Image {self.id} | {self.title}"


class TourPackageDestination(Model):
    tour_package = ForeignKey('TourPackage', CASCADE)
    destination = ForeignKey('Destination', CASCADE)


class TourPackageGallery(Model):
    tour_package = ForeignKey('TourPackage', CASCADE)
    gallery = ForeignKey('Gallery', CASCADE)


class DestinationGallery(Model):
    destination = ForeignKey('Destination', CASCADE)
    gallery = ForeignKey('Gallery', CASCADE)


class TravelPlan(Model):
    tour_package = ForeignKey(TourPackage, on_delete=CASCADE, related_name='travel_plans')
    day_number = PositiveIntegerField(help_text="Sayohatning necha kunligi") # noqa
    plan_title = CharField(max_length=255, help_text="Kunning rejasi uchun sarlavha") # noqa
    plan_description = TextField(help_text="Kunning batafsil tavsifi") # noqa

    class Meta:
        ordering = ['day_number']
        verbose_name = 'Sayohat rejasi' # noqa
        verbose_name_plural = 'Sayohat rejalari' # noqa

    def __str__(self):
        return f"Day {self.day_number} - {self.plan_title}"


class Activity(Model):
    travel_plan = ForeignKey('TravelPlan', on_delete=CASCADE, related_name='activities')
    title = CharField(max_length=255, help_text="Faoliyatning nomi") # noqa
    description = TextField(help_text="Faoliyat haqida qisqacha tavsif") # noqa
    start_time = TimeField(help_text="Faoliyatning boshlanish vaqti") # noqa
    end_time = TimeField(help_text="Faoliyatning tugash vaqti", blank=True, null=True) # noqa
    additional_info = TextField(
        blank=True,
        help_text="Qo'shimcha ma'lumotlar yoki xizmatlar ro'yxati (masalan, transport, ovqatlanish)") # noqa

    class Meta:
        ordering = ['start_time']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title

