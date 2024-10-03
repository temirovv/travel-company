from django.contrib.admin import ModelAdmin, register
from .models import Booking


@register(Booking)
class BookingModelAdmin(ModelAdmin):
    list_display = 'user', 'status', 'id'
