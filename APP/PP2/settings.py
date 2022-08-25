"""
Django settings for PP2 project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config as decouple_config
from decouple import Csv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = decouple_config('django_secret')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple_config('django_debug_state', cast=bool)

ALLOWED_HOSTS = decouple_config('django_allowed_hosts', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # Third party
    'djstripe',
    'django_mathjax',
    'view_breadcrumbs',
    # user added
    'main.apps.MainConfig',
    'user.apps.UserConfig',
    'content.apps.ContentConfig',
    'studentdashboard.apps.StudentdashboardConfig',
    'management.apps.ManagementConfig',
    # native
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
AUTH_USER_MODEL = 'user.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PP2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
               # make your file entry here.
               'filter_tags': 'management.templatetags.general',
            }
        },
    },
]

WSGI_APPLICATION = 'PP2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': decouple_config('DB_ENGINE'),
        'NAME': decouple_config('DB_NAME'),
        'USER': decouple_config('DB_USER'),
        'PASSWORD': decouple_config('DB_PASSWORD'),
        'HOST': decouple_config('DB_HOST'),
        'PORT': decouple_config('DB_PORT', cast=int),
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Groups settings
VALID_GROUPS = [
        "Admin",
        "Student",
        "Teacher",
        "PrivateTutor",
        "School",
        "TuitionCenter",
        "Editor",
        "Affiliate",
    ]
# SMTP settings
EMAIL_BACKEND = decouple_config('EMAIL_BACKEND')
# This uses an installed package to handle sending emails,
# other means dont work for some odd reason
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = decouple_config('SES_endpoint')
EMAIL_PORT = decouple_config('SES_TLS_PORT', cast=int)
EMAIL_HOST_USER = decouple_config('SES_SMTP_USER')
EMAIL_HOST_PASSWORD = decouple_config('SES_PASSWORD')
EMAIL_USE_TLS = decouple_config('SES_USE_TLS', cast=bool)

# Stripe settings
STRIPE_LIVE_SECRET_KEY = decouple_config('Stripe_live_secret')
STRIPE_TEST_SECRET_KEY = decouple_config('Stripe_test_secret')

# Change to True in production
STRIPE_LIVE_MODE = decouple_config('Stripe_live_mode', cast=bool)

# Get it from the section in the Stripe dashboard where
# you added the webhook endpoint
DJSTRIPE_WEBHOOK_SECRET = decouple_config('Stripe_hook_secret')

# We recommend setting to True for new installations
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

# Paypal settings
PAYPAL_MODE = decouple_config('PAYPAL_MODE')
PAYPAL_CLIENT_ID = decouple_config('Paypal_test_client_id')
PAYPAL_CLIENT_SECRET = decouple_config('Paypal_test_client_secret')
PAYPAL_WEBHOOK_ID = decouple_config('Paypal_test_webhook_id')

# Mathjax settings
MATHJAX_ENABLED = True
MATHJAX_CONFIG_DATA = {
      "tex2jax": {
        "inlineMath": [
                ['$', '$'],
                ['\\(', '\\)']
            ]
      }
    }

# Breadcrumb settings
BREADCRUMBS_TEMPLATE = "base/breadcrumbs.html"
BREADCRUMBS_HOME_LABEL = "Home"





