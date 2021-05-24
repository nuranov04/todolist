from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    content = models.CharField(max_length=50)
    data = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-id',)
