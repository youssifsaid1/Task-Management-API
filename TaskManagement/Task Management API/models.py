from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    task=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    comletiondate=models.DateTimeField(auto_now_add=False) 
    def __str__(self):
        return self.task
    class Meta:
        ordering = ['-comletiondate']