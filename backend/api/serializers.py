"""Serializers for API application."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Class meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
