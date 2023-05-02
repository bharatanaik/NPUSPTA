# NPUSPTA settings.py  

from pathlib import Path
from django.core.management.commands.runserver import Command as runserver
runserver.default_port = "8070"


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '6sv^9hz4tyvu#9rf344*)a9#te_qd@v#6c3j#og)up(x6f$@v*'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','npuspta.org', 'www.npuspta.org']


EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'mail@npuspta.org'
EMAIL_HOST_PASSWORD =   "#NPUSPTA~mail2003"
EMAIL_PORT = 587


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


"""PRODUCTION SETTINGS (DEBUG = FALSE)"""
if not DEBUG:
    ALLOWED_HOSTS = ['npuspta.org']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 518400 
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    CSRF_TRUSTED_ORIGINS = ['https://npuspta.org', 'https://www.npuspta.org']


# Application definition
INSTALLED_APPS = [
    'main','bootstrap5','import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
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

ADMIN_EMAILS = ["bharat.anaik2003@gmail.com", "mitheshmoodukonaje@gmail.com"]

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


BOOTSTRAP5 = {"set_placeholder":False}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = '/home/iapshoyw/public_html/static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
