# NPUSPTA settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '6sv^9hz4tyvu#9rf344*)a9#te_qd@v#6c3j#og)up(x6f$@v*'
DEBUG = False
ALLOWED_HOSTS = ['www.npuspta.org', 'npuspta.org']

# email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'mail@npuspta.org'
EMAIL_HOST_PASSWORD = '#NPUSPTA~mail2003'
EMAIL_PORT = 465

# Application definition
INSTALLED_APPS = [
    'main','bootstrap5','import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'vahqwpml_npuspta',
        'USER': 'vahqwpml_bharat',
        'PASSWORD':'data@npuspta2003',
        'HOST':'localhost',
        'PORT':3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

BOOTSTRAP5 = {"set_placeholder":False}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = '/home/vahqwpml/public_html/static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


try:
    from local_settings import *
except:
    pass

