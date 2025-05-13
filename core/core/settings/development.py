from .base import *

# Development database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Additional development-specific settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Celery config
CELERY_RESULT_BACKEND = config(
    "CELERY_RESULT_BACKEND", default="redis://redis:6379/0"
)
