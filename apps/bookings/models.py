# bookings/models.py
from django.contrib.auth import get_user_model
from django.db.models import (
    TextChoices, ForeignKey, Model, CASCADE, CharField,
    PositiveIntegerField, DecimalField, DateField, TextField)

from apps.tour_packages.models import TourPackage


User = get_user_model()


class BookingTicketTypeChoices(TextChoices):
    REGULAR = 'regular', 'Regular'
    VIP = 'vip', 'VIP'


class BookingStatusChoices(TextChoices):
    PENDING = 'pending', 'Pending'
    CONFIRMED = 'confirmed', 'Confirmed'
    CANCELLED = 'cancelled', 'Cancelled'


class Booking(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='bookings')
    tour_package = ForeignKey(TourPackage, on_delete=CASCADE, related_name='bookings')
    ticket_type = CharField(
        max_length=10, choices=BookingTicketTypeChoices.choices,
        db_default=BookingTicketTypeChoices.REGULAR)
    number_of_adults = PositiveIntegerField(default=1)
    number_of_children = PositiveIntegerField(default=0)
    total_price = DecimalField(max_digits=12, decimal_places=2)
    booking_date = DateField()
    status = CharField(
        max_length=10, choices=BookingStatusChoices.choices,
        default=BookingStatusChoices.PENDING)
    message = TextField(blank=True, help_text="Optional message from the user")

    def calculate_total_price(self):
        return (self.tour_package.price * self.number_of_adults) + (
                    self.tour_package.price * 0.5 * self.number_of_children)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
