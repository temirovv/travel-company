import asyncio

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Interest

# bot imports
from apps.places.bot.loader import bot
from apps.places.bot.data.config import ADMIN


async def notify_admin(admin: int, message: str):
    await bot.send_message(admin, text=message)


@receiver(post_save, sender=Interest)
def send_message_via_bot(sender, instance: Interest, created: bool, **kwargs):
    if created:
        message = f"{instance.place.name} ga {instance.phone_number} qiziqish bildirdi"
        print(f'{ADMIN=}')
        for admin in ADMIN:
            print(f'{admin=}')
            print(f'{type(admin)=}')
            asyncio.run(
                notify_admin(admin, message)
            )
