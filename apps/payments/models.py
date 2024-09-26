from django.contrib.auth import get_user_model
from django.db.models import (
    Model, ForeignKey,
    CASCADE, DecimalField,
    CharField, TextChoices, DateTimeField)

User = get_user_model()


class Status(TextChoices):
    PENDING = 'pending', 'Pending'
    PROCESSING = 'processing', 'Processing'
    COMPLETED = 'completed', 'Completed'
    FAILED = 'failed', 'Failed'
    CANCELLED = 'cancelled', 'Cancelled'


class Payment(Model):
    user = ForeignKey(User, CASCADE)
    amount = DecimalField(max_digits=12, decimal_places=2)
    transaction_id = CharField(max_length=255, blank=True, null=True)
    status = CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"



