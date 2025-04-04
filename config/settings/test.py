import environ
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("planty_content")

env = environ.Env()

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "mptt",
    "stdimage",
    "corsheaders",
    "taggit",
    "drf_spectacular",
    "planty_content.apps.PlantyContentConfig",
    "planty_plant_content.apps.PlantyPlantContentConfig",
    "solid_backend.content",
    "solid_backend.contact",
    "solid_backend.glossary",
    "solid_backend.message",
    "solid_backend.slideshow",
    "solid_backend.quiz",
    "solid_backend.photograph",
    "solid_backend.media_object",
    "django_cleanup.apps.CleanupConfig",  # Should be placed last!
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

PROFILES_SERIALIZERS = {
    "wine_related": ("planty_content.serializers", "WineSerializer",),
    "plant_related": ("planty_plant_content.serializers", "PlantSerializer"),
}

INSTALLED_APPS += [
    "django_extensions",
]

# DEBUG
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# SECRET KEY
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="h18i_1j3^d$e6iq8xur&yvbkpk08il9x^&9cf2l2%-0yqx7ss)"
)

# MAIL
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# # DATABASE
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "db_app",
#         "USER": "db_user" if not env("TRAVIS_CI", default=False) else "postgres",
#         "PASSWORD": "db_pass",
#         "HOST": "db" if env("PYTHONBUFFERED", default=False) else "localhost",
#         "PORT": 5432,
#     }
# }

DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql_psycopg2",}}

# CACHING
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "loggers": {
        "werkzeug": {"handlers": ["console"], "level": "DEBUG", "propagate": True,}
    },
}

ALLOWED_HOSTS = ["*"]
