# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0009_auto_20150927_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistTodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('dateCreated', models.DateTimeField(default=datetime.datetime(2015, 9, 27, 21, 9, 7, 252252))),
                ('dateUpdated', models.DateTimeField(null=True)),
                ('dateCompleted', models.DateTimeField(null=True)),
                ('todoDescription', models.CharField(max_length=100, default='Needs a Description')),
                ('checklistId', models.ForeignKey(to='checklists.Checklist')),
            ],
        ),
        migrations.RemoveField(
            model_name='checklisttodos',
            name='checklistId',
        ),
        migrations.DeleteModel(
            name='ChecklistTodos',
        ),
    ]
