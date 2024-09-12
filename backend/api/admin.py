"""Текст чтоб убрать ошибку пип на время спринта."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Текст чтоб убрать ошибку пип на время спринта."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
