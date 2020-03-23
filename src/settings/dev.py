from .base import *

ALLOWED_HOSTS += ['0.0.0.0']
DEBUG = True

WSGI_APPLICATION = 'wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}