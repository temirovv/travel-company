from django.db.models import Model, CharField, BigIntegerField, \
    ForeignKey, CASCADE, TextField, ImageField, FileField
from apps.tour_packages.models import TourPackage


class TelegramChannel(Model):
    chat = CharField(max_length=455, help_text="Telegram kanal usernami yoki aydisi")

    class Meta:
        verbose_name = "Telegram Kanal"
        verbose_name_plural = "Telegram Kanallar"

    def __str__(self):
        return self.chat


class BotAdmin(Model):
    user_id = BigIntegerField(help_text="Adminning telegramdagi user aydisi")

    class Meta:
        verbose_name = "Bot admin"
        verbose_name_plural = "Bot adminlari"


class TourPackageMessage(Model):
    tour_package = ForeignKey(TourPackage, CASCADE)


class ChannelMessage(Model):
    text = TextField()

    def __str__(self):
        return f"Message for channel {self.id}"


class ChannelMessageImage(Model):
    content = ImageField(upload_to='channel_message/', help_text="xabar uchun rasmlar")
    channel_message = ForeignKey(ChannelMessage, CASCADE, related_name='message_images')

    def __str__(self):
        return f"Message for channel {self.channel_message_id}"


class ChannelMessageVideo(Model):
    content = FileField(upload_to='channel_message_videos/', help_text="xabar uchun video")
    channel_message = ForeignKey(ChannelMessage, CASCADE, related_name='message_videos')

    def __str__(self):
        return f"Message for channel {self.channel_message_id}"
