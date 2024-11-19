from root.settings.base import *


load_dotenv(BASE_DIR / '.env/.env.local')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')
print(DEBUG)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

PAYME: dict = {
    'PAYME_ID': os.getenv("PAYME_ID"),
    'PAYME_KEY': os.getenv("PAYME_KEY"),
    'PAYME_URL': os.getenv("PAYME_URL"),
    'PAYME_CALL_BACK_URL': os.getenv("PAYME_CALL_BACK_URL"),
    'PAYME_MIN_AMOUNT': int(os.getenv("PAYME_MIN_AMOUNT", default=0)),
    'PAYME_ACCOUNT': os.getenv("PAYME_ACCOUNT"),
}

BOT_ADMINS = os.getenv('BOT_ADMINS', '*').split(',')
