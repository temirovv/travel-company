# translation.py
from modeltranslation.translator import translator, TranslationOptions, register
from .models import TourPackage, TravelPlan, Destination


@register(TourPackage)
class TourPackageTranslationOptions(TranslationOptions):
    fields = 'title', 'description'


@register(TravelPlan)
class TravelPlanTranslationOptions(TranslationOptions):
    fields = 'plan_title', 'plan_description'


@register(Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = 'name', 'description'
