import asyncio
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from aiogram.utils.media_group import MediaGroupBuilder
from django.db import transaction

from .models import TelegramChannel, BotAdmin, TourPackageMessage, ChannelMessage
from .loader import send_message_to_channels, make_media_group, build_full_media_urls
from .bot_messages import make_package_detail_msg


# @receiver(post_save, sender=TelegramChannel)
# def send_message_via_bot(sender, instance: TelegramChannel, created: bool, **kwargs):
#     pass
# 
# 
# @receiver(post_save, sender=TourPackageMessage)
# def send_tour_package_2_telegram_channels(sender, instance: TourPackageMessage, created: bool, **kwargs):
#     if created:
#         channels = TelegramChannel.objects.all()
#         tour_package = instance.tour_package
# 

@receiver(post_save, sender=ChannelMessage)
def send_message_2_telegram_channel2(sender, instance: ChannelMessage, created: bool, **kwargs):
    if created:
        transaction.on_commit(lambda: process_channel_message(instance))


def process_channel_message(instance, request=None):
    """
    Processes a ChannelMessage instance after it has been fully saved along with its related objects.
    """
    channels = [channel.chat for channel in TelegramChannel.objects.all()]
    all_images, all_videos = build_full_media_urls(instance, request)

    print(f"{all_images=}\n{all_videos=}")

    if all_images or all_videos:
        media = MediaGroupBuilder(caption=instance.text)
        if all_images:
            media = make_media_group(media, media_type='photo', files=all_images)
        if all_videos:
            media = make_media_group(media, media_type='video', files=all_videos)
        asyncio.run(send_message_to_channels(channels, media=media))
    else:
        asyncio.run(send_message_to_channels(channels, message=instance.text))
