from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import (
    TourPackage, Destination,
    Gallery, TravelPlan,
    Activity, TourPackageGallery,
    TourPackageDestination, DestinationGallery
)
from modeltranslation.admin import TranslationAdmin


class TourPackageGalleryStackedInline(StackedInline):
    model = TourPackageGallery


class TourPackageDestinationStackedInline(StackedInline):
    model = TourPackageDestination


class DestinationGalleryStackedInline(StackedInline):
    model = DestinationGallery


class TravelPlanStackedInline(StackedInline):
    model = TravelPlan


class ActivityStackedInline(StackedInline):
    model = Activity


@register(TourPackage)
class TourPackageModelAdmin(ModelAdmin):
    inlines = TourPackageGalleryStackedInline, TourPackageDestinationStackedInline, TravelPlanStackedInline


@register(Destination)
class DestinationModelAdmin(ModelAdmin):
    inlines = DestinationGalleryStackedInline,


@register(Gallery)
class GalleryModelAdmin(ModelAdmin):
    pass


@register(TravelPlan)
class TravelPlanModelAdmin(ModelAdmin):
    inlines = ActivityStackedInline,


# register(TourPackage, TourPackageModelAdmin)
