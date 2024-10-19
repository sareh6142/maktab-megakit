from config.settings import *

SECRET_KEY = 'django-insecure-_$8l0u11l6515yl6w+o==gwrk(6l#auc&3^69)frw*nfl-p)t+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


MEDIA_ROOT = BASE_DIR/ 'media'
STATIC_ROOT = BASE_DIR/ 'static'


STATICFILES_DIRS = [
    BASE_DIR/ 'statics',
]

X_FRAME_OPTION = 'SAMEORIGIN'