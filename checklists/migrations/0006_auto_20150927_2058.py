# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0005_checklisttodos_datecompleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklisttodos',
            name='todoItemId',
        ),
        migrations.AddField(
            model_name='checklisttodos',
            name='todoDescription',
            field=models.CharField(default='Needs a Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='checklisttodos',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 20, 58, 30, 544417)),
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
    ]
