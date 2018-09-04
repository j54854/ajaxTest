from django.db import models
from django.utils import timezone


class Todo(models.Model):
    task = models.CharField(max_length=255, unique=True)
    due = models.DateTimeField()
    done = models.BooleanField()

    def __str__(self):
        return self.task
