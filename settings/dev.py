from .base import *

ALLOWED_HOSTS += ['0.0.0.0']
DEBUG = True

WSGI_APPLICATION = 'wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }   
}