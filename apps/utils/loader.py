from aiogram.utils.media_group import MediaGroupBuilder

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from apps.utils.bot.main import dp, bot


async def send_message_to_admin(message: str) -> None:
    """
    Admin uchun bot orqali xabar jo'natish funksiyasi
    :param message: str
    :return: None
    """
    for chat in settings.BOT_ADMINS:
        await bot.send_message(chat_id=chat, text=message)


def make_media_group(media: MediaGroupBuilder, media_type: str, files):
    for file in files:
        media.add(type=media_type, media=file)

    return media


async def send_message_to_channels(channels: list, **kwargs) -> None:
    """
    telegram kanallar va gruppalariga xabar jo'natish
    :param channels: list
    :return: None
    """
    print(f"{channels=}\n{kwargs=}")
    if kwargs:
        media: MediaGroupBuilder = kwargs.get('media')
        message = kwargs.get('message')
        if media:
            print('media keldi')
            for chat in channels:
                async with bot as b:
                    await b.send_media_group(chat_id=chat, media=media.build())
        elif message:
            for chat in channels:
                async with bot as b:
                    await b.send_message(chat_id=chat, text=message)
        else:
            raise KeyError('message yoki media topilmadi')
    else:
        raise KeyError("missing message or media")


def get_full_media_url(file_url, request=None):
    """
    Build a fully specified URL for a media file.
    Uses the request object if available, otherwise falls back to SITE_URL.
    """
    if request:
        domain = get_current_site(request).domain
        protocol = 'https' if request.is_secure() else 'http'
        return f"{protocol}://{domain}{file_url}"
    return f"{settings.SITE_URL}{file_url}"


def build_full_media_urls(instance, request=None):
    """
    Generate lists of fully specified URLs for images and videos.
    """
    all_images = [get_full_media_url(image.content.url, request) for image in instance.message_images.all()]
    all_videos = [get_full_media_url(video.content.url, request) for video in instance.message_videos.all()]
    return all_images, all_videos
