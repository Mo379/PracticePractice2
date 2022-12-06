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
import boto3


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = decouple_config('django_secret')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple_config('django_debug_state', cast=bool)
if DEBUG == False:
    PREPEND_WWW = True
ALLOWED_HOSTS = decouple_config('django_allowed_hosts', cast=Csv())
# CND and S3 vars
CSRF_TRUSTED_ORIGINS = decouple_config('CSRF_TRUSTED_ORIGINS', cast=Csv())
AWS_username = decouple_config('aws_data_user_name')
AWS_access = decouple_config('aws_data_access_key_id')
AWS_secret = decouple_config('aws_data_secret_access_key')
AWS_region = decouple_config('aws_data_region')

# S3 Objects
AWS_DB_BACKUP_BUCKET_NAME = decouple_config('aws_db_backup_bucket')
AWS_BUCKET_NAME = decouple_config('aws_data_bucket')
AWS_S3_C = boto3.client(
        's3',
        aws_access_key_id=AWS_access,
        aws_secret_access_key=AWS_secret
    )
AWS_S3_R = boto3.resource(
        's3',
        aws_access_key_id=AWS_access,
        aws_secret_access_key=AWS_secret
    )
AWS_BUCKET_OBJECT = AWS_S3_R.Bucket(name=AWS_BUCKET_NAME)


# Application definition
INSTALLED_APPS = [
    # Third party
    'djstripe',
    'view_breadcrumbs',
    'multiselectfield',
    'dbbackup',
    # user added
    'main.apps.MainConfig',
    'user.apps.UserConfig',
    'content.apps.ContentConfig',
    'dashboard.apps.dashboardConfig',
    'management.apps.ManagementConfig',
    # native
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]
AUTH_USER_MODEL = 'user.User'
SITE_URL = decouple_config('Site_domain')
SITE_ID = 1
CDN_URL = decouple_config('CDN_URL')
# DB backup
DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': AWS_access,
    'secret_key': AWS_secret,
    'bucket_name': AWS_DB_BACKUP_BUCKET_NAME,
    'default_acl': 'private',
}


#
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
DBBACKUP_CONNECTORS = {
    'default': {
        'ENGINE': decouple_config('DB_ENGINE'),
        'NAME': decouple_config('DB_NAME'),
        'USER': decouple_config('DB_USER'),
        'PASSWORD': decouple_config('DB_PASSWORD'),
        'HOST': decouple_config('DB_HOST'),
        'PORT': decouple_config('DB_PORT', cast=int),
    }
}
DBBACKUP_CONNECTOR_MAPPING = {
    'transaction_hooks.backends.postgis': 'dbbackup.db.postgresql.PgDumpGisConnector',
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


# Google API settings
GOOGLE_API_KEY = 'None'
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
STRIPE_LIVE_PUBLISHABLE_KEY = decouple_config('Stripe_live_publishable')
#
STRIPE_TEST_SECRET_KEY = decouple_config('Stripe_test_secret')
STRIPE_TEST_Publishable_KEY = decouple_config('Stripe_test_publishable')

# Change to True in production
STRIPE_LIVE_MODE = decouple_config('Stripe_live_mode', cast=bool)
if STRIPE_LIVE_MODE:
    STRIPE_SECRET_KEY = decouple_config('Stripe_live_secret')
    STRIPE_PUBLISHABLE_KEY = decouple_config('Stripe_live_publishable')
else:
    STRIPE_SECRET_KEY = decouple_config('Stripe_test_secret')
    STRIPE_PUBLISHABLE_KEY = decouple_config('Stripe_test_publishable')

# Get it from the section in the Stripe dashboard where
# you added the webhook endpoint
DJSTRIPE_WEBHOOK_SECRET = decouple_config('Stripe_webhook_secret')

# We recommend setting to True for new installations
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

# Paypal settings
PAYPAL_MODE = decouple_config('PAYPAL_MODE')
PAYPAL_CLIENT_ID = decouple_config('Paypal_test_client_id')
PAYPAL_CLIENT_SECRET = decouple_config('Paypal_test_client_secret')
PAYPAL_WEBHOOK_ID = decouple_config('Paypal_test_webhook_id')

# Breadcrumb settings
BREADCRUMBS_TEMPLATE = "base/breadcrumbs.html"
BREADCRUMBS_HOME_LABEL = "Home"


# Markdown editor settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'
IMAGE_FILE_FORMAT = ['png', 'jpg', 'jpeg', 'webp']




# Celery settings
CELERY_BROKER_URL = decouple_config('Celery_Broker')
CELERY_RESULT_BACKEND = decouple_config('Celery_Result')
