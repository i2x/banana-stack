# settings.py

from pathlib import Path
import os
from dotenv import load_dotenv
from distutils.util import strtobool

# load .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # โฟลเดอร์รวบรวมไฟล์ static หลัง collectstatic

# Media (ถ้าใช้)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv('DJANGO_DEBUG', 'False')))


def csv_env(name, default=""):
    val = os.getenv(name, default)
    return [x.strip() for x in val.split(",") if x.strip()]

ALLOWED_HOSTS = csv_env("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1")


CSRF_TRUSTED_ORIGINS = csv_env(
    "CSRF_TRUSTED_ORIGINS",
    "http://localhost"
)

# ถ้าใช้ HTTPS หลัง Nginx/Proxy
_secure_proxy = os.getenv("SECURE_PROXY_SSL_HEADER")
if _secure_proxy:
    k, v = [s.strip() for s in _secure_proxy.split(",", 1)]
    SECURE_PROXY_SSL_HEADER = (k, v)

CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "False") == "True"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False") == "True"



# Application definition

INSTALLED_APPS = [
    'banana_api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'rest_framework',
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'banana_api.utils.custom_exception_handler.custom_exception_handler',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "")
if CORS_ALLOWED_ORIGINS:
    CORS_ALLOWED_ORIGINS = [origin.strip() for origin in CORS_ALLOWED_ORIGINS.split(",")]
else:
    CORS_ALLOWED_ORIGINS = []

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DooKluayWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DooKluayWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# ซ่อนข้อมูล Database ทั้งหมด
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432') # ใส่ค่า default ไว้เผื่อไม่มีใน .env
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


