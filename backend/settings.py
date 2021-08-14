"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

import pymongo
from corsheaders.defaults import default_headers

import dj_database_url
import django_heroku
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'authenticator.authbackend.CustomAuthentication']}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'https://collabconnect-development.firebaseapp.com',
    'https://collabamigo-testing.web.app/',
    'https://collabamigo.com',
    'https://www.collabamigo.com'
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'aeskey',
    'token',
    'iv'
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

# TODO: Insecure ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# DataFlair neeche hai
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("PASS_KEY")

# Application definition hai ye
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'connect.apps.ConnectConfig',
    'corsheaders',
    'autocomplete',
    'club',
]

# TODO: Enable CSRF
MIDDLEWARE = [
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

APPEND_SLASH = True

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

v1 = 'django.contrib.auth.password_validation.'
v2 = 'UserAttributeSimilarityValidator'
v3 = v1 + v2

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': v3,
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

FRONTEND_URL = "https://collabconnect-development.firebaseapp.com" if DEBUG \
    else "https://collabconnect.web.app"

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


# CSRF_COOKIE_SECURE = bool(os.getenv("PRODUCTION"))
SECURE_SSL_REDIRECT = bool(os.getenv("PRODUCTION"))
SESSION_COOKIE_SECURE = bool(os.getenv("PRODUCTION"))

if os.environ['EMAIL'] != "a":
    MongoClient = pymongo.MongoClient(os.environ['MONGODB_URI'])


ALLOWED_IN_DEBUG = ['adityapratapsingh51@gmail.com',
                    'aditya20016@iiitd.ac.in', 'shikhar20121@iiitd.ac.in',
                    'heemank20064@iiitd.ac.in', 'heemankv@gmail.com',
                    'anis20026@iiitd.ac.in', 'vishwesh20156@iiitd.ac.in', ]

DATABASES = dict()
DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=False)
django_heroku.settings(locals(), databases=False)
