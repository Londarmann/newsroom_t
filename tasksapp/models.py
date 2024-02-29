from datetime import datetime
from django.db import models

from menu.models import MenuModel


# from taskmanager.menu.models import Menu

# from menu.models import Menu


class TaskName(models.Model):
    task_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True, default=None)
    task_text = models.TextField()
    fkey = models.ForeignKey(MenuModel, on_delete=models.CASCADE)




