"""
Django settings for SPCM project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kj4maq(_q2s%9tq#cuq-c8*0fxd%!0u+d$-i*5gd%7absy2do8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost:4200', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'spcmapp',
    'corsheaders',
    'storages',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'spcmapp.middleware.JWTAuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'SPCM.urls'

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

WSGI_APPLICATION = 'SPCM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spcm',  
        'USER': 'root', 
        'PASSWORD': '',  
        'HOST': 'localhost',    
        'PORT': '3306',         
        
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
AUTHENTICATION_BACKENDS = (
    'spcmapp.authentication.EmailBackend',  
    'django.contrib.auth.backends.ModelBackend', 
)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=4),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),  
    'ROTATE_REFRESH_TOKENS': False, 
    'BLACKLIST_AFTER_ROTATION': True, 
}

AUTH_USER_MODEL = 'spcmapp.User'


# settings.py

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'DO00H69G2ZGQJC6LBUUN'
AWS_SECRET_ACCESS_KEY = 'rHtA3ByDGGBCH3t27LzbkGwrl4wWHZGUYK+cPD1d8z0'
AWS_STORAGE_BUCKET_NAME = 'clayenss'
AWS_S3_ENDPOINT_URL = 'https://clayenss.nyc3.digitaloceanspaces.com'
AWS_S3_REGION_NAME = 'nyc3'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'media'

SPACES_REGION = 'nyc3'
SPACES_ENDPOINT_URL = 'https://clayenss.nyc3.digitaloceanspaces.com'
SPACES_ACCESS_KEY_ID = 'DO00H69G2ZGQJC6LBUUN'
SPACES_SECRET_ACCESS_KEY = 'rHtA3ByDGGBCH3t27LzbkGwrl4wWHZGUYK+cPD1d8z0'
SPACES_BUCKET_NAME = 'clayenss'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'          # Servidor SMTP de Gmail (o el de tu proveedor)
EMAIL_PORT = 587                       # Puerto para TLS
EMAIL_USE_TLS = True                   # Habilitar TLS
EMAIL_HOST_USER = 'clayens82@gmail.com' # Tu correo electrónico
EMAIL_HOST_PASSWORD = 'lgfc mzle bnrw zocx'   # Contraseña del correo electrónico
DEFAULT_FROM_EMAIL = 'clayens82@gmail.com'  # Dirección del remitente


# STATIC_ROOT = '/web/spcm/SPCM_BACK/static/'
# MEDIA_ROOT = '/web/spcm/SPCM_BACK/media/'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
