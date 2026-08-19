
import os
from decouple import config
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).parent
EVENTPROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ag8flu0f6c0dzcatyax_nftf-9v)amp2eee6#^fo64r4+q-iks'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agendaapps.authentication',
    'agendaapps.home',
    'agendaapps.custom',
    'agendaapps.institute',
    'agendaapps.event',
    'agendaapps.reports',
    'crispy_forms',
    'bootstrap4',
    'crispy_bootstrap4',
    'bootstrap_datepicker_plus',
    'mathfilters',
    "ckeditor",
    "tinymce",
    'django_summernote',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'agenda.middleware.AgendaSSOMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agenda.urls'
# LOGIN_REDIRECT_URL = "home"   # Route defined in home/urls.py
# LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(EVENTPROJECT_DIR, "agendaapps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'agenda.context.menu_home',
            ],
        },
    },
]

WSGI_APPLICATION = 'agenda.wsgi.application'
AUTH_USER_MODEL = 'authentication.User'

CSRF_TRUSTED_ORIGINS = [
    "https://agenda.mop1.gov.tl",
    "https://mop1.gov.tl",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'smartv04_agenda',
        'USER': 'root',
        'PASSWORD': 'atauro2630',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        },
    },

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db26_agendamop',
    #     'USER': 'admindbmop5',
    #     'PASSWORD': 'M0pAdmin#2026#',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         "init_command": "SET foreign_key_checks = 0;",
    #     },
    # },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/


LANGUAGE_CODE = 'en-us'
USE_I18N = True
TIME_ZONE = "Asia/Dili"
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(EVENTPROJECT_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(EVENTPROJECT_DIR, 'agendaapps/static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(EVENTPROJECT_DIR, 'agendaapps/media')
X_FRAME_OPTIONS = 'SAMEORIGIN'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

BASE_DIRs = Path(__file__).resolve().parent


SESSION_ENGINE = "django.contrib.sessions.backends.db"

SESSION_COOKIE_NAME = "agenda_sessionid"
SESSION_COOKIE_AGE = 36000
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True

SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = "Lax"


# Load PUBLIC key
with open(BASE_DIRs / "key" / "public.pem", "r") as f:
    PUBLIC_KEY = f.read()

SIMPLE_JWT = {
    "ALGORITHM": "RS256",
    "VERIFYING_KEY": PUBLIC_KEY,
    "SIGNING_KEY": None,
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "info.agenda.mop@gmail.com"
EMAIL_HOST_PASSWORD = "evciqxagmvckssif"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER