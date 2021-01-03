import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, '..'))

MEDIA_ROOT = os.path.join(BASE_DIR, 'testproject', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'testproject', 'static')


SECRET_KEY = 'testsecretkey'
X_FRAME_OPTIONS = 'SAMEORIGIN'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

LANGUAGE_CODE = 'de'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = 'testproject.wsgi.application'
ROOT_URLCONF = 'testproject.urls'

STATIC_URL = '/static/'

INSTALLED_APPS = [
    'text_ckeditor',
    'text_ckeditor.text_ckeditor_links',
    'testproject.testapp',
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

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'testproject', 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # NOQA
]
