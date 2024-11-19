import asyncio

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse

from payme.models import MerchantTransactionsModel
from .models import Booking, BookingStatusChoices
from apps.utils.bot_messages import make_msg_admin
from apps.utils.loader import send_message_to_admin


@receiver(post_save, sender=Booking)
def model_updated(sender, instance: Booking, created: bool, **kwargs):
    if not created:
        if instance.status == BookingStatusChoices.CONFIRMED:
            package_detail = settings.HOST_IN_USE + reverse(
                'package_detail', kwargs={'slug': instance.tour_package.slug})
            transaction_id = MerchantTransactionsModel.objects.get(order_id=instance.id)
            transaction_check = settings.PAYMENT_CHECKS + str(transaction_id)
            message = make_msg_admin(
                instance.phone_number, instance.tour_package.title,
                instance.amount, instance.id, transaction_check,
                instance.booking_date, instance.message, package_detail
            )
            asyncio.run(send_message_to_admin(message))

