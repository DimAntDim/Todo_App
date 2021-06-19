from django.db import models
from django.db.models.deletion import CASCADE

class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Todo(models.Model):
    task_name = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(Person, on_delete=CASCADE)
    description = models.TextField(blank=False)

    status = models.BooleanField(
        default=False,
        )

    date = models.DateTimeField(
        null=True,
    )
    
    def __str__(self):
        return self.task_name
