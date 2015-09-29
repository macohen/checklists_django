from django.db import models

class Checklist(models.Model):
    checklistId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ChecklistTodo(models.Model):
    todoId = models.AutoField(primary_key=True, db_column='id')
    checklistId = models.ForeignKey(Checklist)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(null=True, blank=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    todoDescription = models.CharField(max_length=100,default='Needs a Description')

    def __str__(self):
        return self.todoDescription




