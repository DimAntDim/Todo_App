from django.db import models


class Todo(models.Model):
    creator = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.creator
