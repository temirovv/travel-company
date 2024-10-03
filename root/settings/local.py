from root.settings.base import *


load_dotenv(BASE_DIR / '.env/.env.local')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = list(os.getenv('ALLOWED_HOSTS', '*'))

