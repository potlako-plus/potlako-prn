"""
Django settings for potlako_prn project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import configparser
import os
import sys

from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()

ETC_DIR = '/etc'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = 'potlako_prn'
SITE_ID = 1

ETC_DIR = os.path.join(BASE_DIR, 'etc')

CONFIG_FILE = f'potlako.ini'

CONFIG_PATH = os.path.join('/etc', 'potlako', CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gc2s5qt4g7(&scfo8xqra6wrn0%a!io4)g^yp@*nwa4e1hre7_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')

ALLOWED_HOSTS = []

# EDC SMS configuration
BASE_API_URL = config['edc_sms']['base_api_url']

# Application definition

INSTALLED_APPS = [
    'django_q',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework.authtoken',
    'django_crypto_fields.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_sync.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_protocol.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'potlako_subject.apps.AppConfig',
    'potlako_visit_schedule.apps.AppConfig',
    'potlako_prn.apps.EdcFacilityAppConfig',
    'potlako_prn.apps.EdcAppointmentAppConfig',
    'potlako_prn.apps.EdcVisitTrackingAppConfig',
    'potlako_prn.apps.EdcSmsAppConfig',
    'potlako_prn.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'potlako_prn.urls'

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

WSGI_APPLICATION = 'potlako_prn.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COUNTRY = 'botswana'

DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'potlako_dashboard:subject_listboard_url',
    'screening_listboard_url': 'potlako_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'potlako_dashboard:subject_dashboard_url',
}

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

COMMUNITIES = config['communities']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

