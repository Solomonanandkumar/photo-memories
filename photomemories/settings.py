from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key-for-local"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "albums",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "photomemories.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "albums" / "templates" ],
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

WSGI_APPLICATION = "photomemories.wsgi.application"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [ BASE_DIR / "albums" / "static" ]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = True