# translation.py
from modeltranslation.translator import translator, TranslationOptions, register
from .models import TourPackage, TravelPlan


@register(TourPackage)
class TourPackageTranslationOptions(TranslationOptions):
    fields = 'title', 'description'


@register(TravelPlan)
class TravelPlanTranslationOptions(TranslationOptions):
    fields = 'plan_title', 'plan_description'
