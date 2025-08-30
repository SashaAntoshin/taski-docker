"""App configuration for API."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """App conf."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
