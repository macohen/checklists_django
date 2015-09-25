import datetime
from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    todoItemId = models.AutoField(primary_key=True)
    description=models.CharField(max_length=100, default='A Thing To Do')

class Checklist(models.Model):
    checklistId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

class ChecklistTodos(models.Model):
    todoItemId = models.ForeignKey(TodoItem)
    checklistId = models.ForeignKey(Checklist)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateUpdated = models.DateTimeField(null=True)




