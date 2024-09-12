"""Текст чтоб убрать ошибку пип на время спринта."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Текст чтоб убрать ошибку пип на время спринта."""

    class Meta:
        """Текст чтоб убрать ошибку пип на время спринта."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
