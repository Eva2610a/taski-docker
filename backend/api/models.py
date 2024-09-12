"""Текст чтоб убрать ошибку пип на время спринта."""
from django.db import models


class Task(models.Model):
    """Текст чтоб убрать ошибку пип на время спринта."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
