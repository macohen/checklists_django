# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0010_auto_20150927_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklisttodo',
            name='id',
        ),
        migrations.AddField(
            model_name='checklisttodo',
            name='todoId',
            field=models.AutoField(serialize=False, default=1, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checklisttodo',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checklisttodo',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 0, 35, 3, 307663)),
        ),
        migrations.AlterField(
            model_name='checklisttodo',
            name='dateUpdated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
