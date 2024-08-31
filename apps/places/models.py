from django.db.models import (
    Model, CharField, ManyToManyField, ForeignKey, CASCADE,
    TextField, DateTimeField, ImageField, DecimalField, SET_NULL
)


class Category(Model):
    name = CharField(max_length=100)
    description = TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Place(Model):
    name = CharField(max_length=255)
    description = TextField()
    location = CharField(max_length=300)
    latitude = DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    categories = ManyToManyField('Category', through='PlaceCategories', related_name='places')

    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'

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
    place = ForeignKey('Place', CASCADE,  'images')
    image = ImageField(upload_to='places/')
    caption = CharField(max_length=255, blank=True, null=True)
    uploaded_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Joy rasmi'
        verbose_name_plural = 'Joy rasmlari'

    def __str__(self):
        return f'{self.place.name} ning rasmi'


class Interest(Model):
    place = ForeignKey('Place', SET_NULL, 'interests', null=True, blank=True)
    phone_number = CharField(max_length=20)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Qiziqish bildirganlar'

    def __str__(self):
        return f"{self.phone_number} raqami {self.place.name} ga qiziqish bildirdi"
