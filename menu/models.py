from django.db import models


class MenuModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name
