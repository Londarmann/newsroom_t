from datetime import datetime

from django.db import models

from tasksapp.models import TaskName


class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    finish_date = models.TimeField(default=datetime.now, null=True, blank=True)
    reference_to_task = models.ForeignKey(TaskName, on_delete=models.CASCADE, blank=False, null=False)
