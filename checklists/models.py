from django.db import models

# Create your models here.
class Checklist(models.Model):
    title = models.CharField(max_length=100)
    #todo_items = models.CharField(max_length=1)
