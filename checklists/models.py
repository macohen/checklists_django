import datetime
from django.db import models

class TodoItem(models.Model):
    todoItemId = models.AutoField(primary_key=True)
    description=models.CharField(max_length=100, default='A Thing To Do')

class Checklist(models.Model):
    checklistId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

class ChecklistTodos(models.Model):
    todoItemId = models.ForeignKey(TodoItem)
    checklistId = models.ForeignKey(Checklist)
    dateCreated = models.DateTimeField(default=datetime.datetime.now())
    dateUpdated = models.DateTimeField(null=True)




