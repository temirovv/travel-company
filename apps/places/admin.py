from django.contrib.admin import ModelAdmin, register, TabularInline
from .models import Category, Place, PlaceImage, Interest


class PlaceImageTabularInline(TabularInline):
    model = PlaceImage
    extra = 1


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@register(Place)
class PlaceModelAdmin(ModelAdmin):
    inlines = PlaceImageTabularInline,


@register(Interest)
class InterestModelAdmin(ModelAdmin):
    pass
