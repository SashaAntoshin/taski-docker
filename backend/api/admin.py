"""Admin configuration for API models."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Class task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
