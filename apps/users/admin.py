from django.contrib.admin import register, ModelAdmin
from .models import User


@register(User)
class UserModelAdmin(ModelAdmin):
    pass
