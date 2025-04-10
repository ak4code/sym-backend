from config.settings.base import BASE_DIR, env

DEBUG = env.bool('DEBUG', default=True)


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'