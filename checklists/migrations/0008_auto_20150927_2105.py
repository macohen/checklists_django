# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0007_auto_20150927_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistTodos',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('dateCreated', models.DateTimeField(default=datetime.datetime(2015, 9, 27, 21, 5, 21, 594002))),
                ('dateUpdated', models.DateTimeField(null=True)),
                ('dateCompleted', models.DateTimeField(null=True)),
                ('todoDescription', models.CharField(max_length=100, default='Needs a Description')),
                ('checklistId', models.ForeignKey(to='checklists.Checklist')),
            ],
        ),
        migrations.RemoveField(
            model_name='checklisttodo',
            name='checklistId',
        ),
        migrations.DeleteModel(
            name='ChecklistTodo',
        ),
    ]
