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
                ('checklistId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistTodo',
            fields=[
                ('todoId', models.AutoField(primary_key=True, db_column='id', serialize=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(null=True, blank=True)),
                ('dateCompleted', models.DateTimeField(null=True, blank=True)),
                ('todoDescription', models.CharField(default='Needs a Description', max_length=100)),
                ('checklistId', models.ForeignKey(to='checklists.Checklist')),
            ],
        ),
    ]
