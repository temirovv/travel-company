from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import TelegramChannel, BotAdmin, TourPackageMessage, \
    ChannelMessage, ChannelMessageImage, ChannelMessageVideo


class ChannelMessageImageStackedInline(StackedInline):
    model = ChannelMessageImage


class ChannelMessageVideoStackedInline(StackedInline):
    model = ChannelMessageVideo


@register(ChannelMessage)
class ChannelMessageModelAdmin(ModelAdmin):
    inlines = ChannelMessageImageStackedInline, ChannelMessageVideoStackedInline


@register(BotAdmin)
class BotAdminModelAdmin(ModelAdmin):
    pass


@register(TourPackageMessage)
class TourPackageMessageModelAdmin(ModelAdmin):
    pass


@register(TelegramChannel)
class TelegramChannelModelAdmin(ModelAdmin):
    pass
