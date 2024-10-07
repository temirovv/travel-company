from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db.models import (
    TextChoices, ForeignKey, Model, CASCADE, CharField,
    PositiveIntegerField, DecimalField, DateField, TextField, EmailField)

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
    user = ForeignKey(User, on_delete=CASCADE, related_name='bookings', null=True, blank=True)
    tour_package = ForeignKey(TourPackage, on_delete=CASCADE, related_name='bookings')
    ticket_type = CharField(
        max_length=10, choices=BookingTicketTypeChoices.choices,
        default=BookingTicketTypeChoices.REGULAR)
    number_of_adults = PositiveIntegerField(default=1)
    number_of_children = PositiveIntegerField(default=0)
    amount = DecimalField(max_digits=12, decimal_places=2)
    phone_number = CharField(max_length=15, help_text="User's phone number")
    email = EmailField()
    booking_date = DateField()
    status = CharField(
        max_length=10, choices=BookingStatusChoices.choices,
        default=BookingStatusChoices.PENDING)
    message = TextField(blank=True, help_text="Optional message from the user")

    def calculate_total_price(self):
        adult_price = Decimal(self.tour_package.price) * Decimal(self.number_of_adults)
        return adult_price

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} {self.id}"
