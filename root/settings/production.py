import os

from root.settings.base import *


load_dotenv(BASE_DIR / '.env/.env.production')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
# ALLOWED_HOSTS = ['bilolhonesttravel.uz', 'www.bilolhonesttravel.uz', 'https://bilolhonesttravel.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PG_NAME'),
        'USER': os.getenv('PG_USER'),
        'PASSWORD': os.getenv('PG_PASSWORD'),
        'HOST': os.getenv('PG_HOST'),
        'PORT': os.getenv('PG_PORT'),
        "TEST": {
            "MIRROR": "default",
        },
    }
}

PAYME: dict = {  # noqa
    'PAYME_ID': os.getenv("PAYME_ID"),
    'PAYME_KEY': os.getenv("PAYME_KEY"),
    'PAYME_URL': os.getenv("PAYME_URL"),
    'PAYME_CALL_BACK_URL': os.getenv("PAYME_CALL_BACK_URL"),
    'PAYME_MIN_AMOUNT': int(os.getenv("PAYME_MIN_AMOUNT", default=0)),
    'PAYME_ACCOUNT': os.getenv("PAYME_ACCOUNT"),
}

BOT_ADMINS = os.getenv('BOT_ADMINS', '*').split(',')
