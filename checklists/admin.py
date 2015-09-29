from django.contrib import admin
from .models import Checklist, ChecklistTodo#, TodoItem

# Register your models here.
admin.site.register(Checklist)
admin.site.register(ChecklistTodo)
#admin.site.register(TodoItem)
