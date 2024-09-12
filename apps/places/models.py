from django.db.models import (
    Model, CharField, ManyToManyField, ForeignKey, CASCADE,
    TextField, DateTimeField, ImageField, DecimalField, SET_NULL, SlugField
)
from django.db.models.functions import Now
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    name = CharField(max_length=100)
    description = TextField(null=True, blank=True)
    slug = SlugField(unique=True, editable=False)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Place(Model):
    name = CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')
    location = CharField(max_length=300)
    latitude = DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    categories = ManyToManyField('Category', through='PlaceCategories', related_name='places')
    slug = SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'
        ordering = '-id',

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def first_image(self):
        first = self.images.first()
        if first:
            return first.image.url
        return ''

    def __str__(self):
        return self.name


class PlaceCategories(Model):
    place = ForeignKey('Place', CASCADE)
    category = ForeignKey('Category', CASCADE)

    class Meta:
        verbose_name = 'Joy Kategoriyasi'
        verbose_name_plural = 'Joy Kategoriyalari'

    def __str__(self):
        return f"{self.place.name} - {self.category.name}"


class PlaceImage(Model):
    place = ForeignKey('Place', CASCADE, related_name='images')
    image = ImageField(upload_to='places/')
    caption = CharField(max_length=255, blank=True, null=True)
    uploaded_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Joy rasmi'
        verbose_name_plural = 'Joy rasmlari'

    def __str__(self):
        return f'{self.place.name} ning rasmi'


class Interest(Model):
    place = ForeignKey('Place', SET_NULL, related_name='interests', null=True, blank=True)
    phone_number = CharField(max_length=20)
    message = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True, db_default=Now())

    class Meta:
        verbose_name_plural = 'Qiziqish bildirganlar'

    def __str__(self):
        return f"{self.phone_number} raqami {self.place.name} ga qiziqish bildirdi"
