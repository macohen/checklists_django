from django.db import models
from django.utils import timezone

class Checklist(models.Model):
    checklistId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ChecklistTodo(models.Model):
    todoId = models.AutoField(primary_key=True)
    checklistId = models.ForeignKey(Checklist)
    dateCreated = models.DateTimeField(default=timezone.now())
    dateUpdated = models.DateTimeField(null=True, blank=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    todoDescription = models.CharField(max_length=100,default='Needs a Description')

    def __str__(self):
        return self.todoDescription




