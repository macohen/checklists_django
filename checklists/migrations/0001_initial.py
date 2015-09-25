# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('checklistId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistTodos',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('checklistId', models.ForeignKey(to='checklists.Checklist')),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('todoItemId', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, default='A Thing To Do')),
            ],
        ),
        migrations.AddField(
            model_name='checklisttodos',
            name='todoItemId',
            field=models.ForeignKey(to='checklists.TodoItem'),
        ),
    ]
