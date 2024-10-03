from root.settings.base import *


load_dotenv(BASE_DIR / '.env/.env.local')

SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG = os.getenv('DEBUG')
# DEBUG = True
# ALLOWED_HOSTS = list(os.getenv('ALLOWED_HOSTS', '*'))
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
