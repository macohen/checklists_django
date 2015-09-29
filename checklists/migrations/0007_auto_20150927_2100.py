# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django import utils


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0006_auto_20150927_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklisttodos',
            name='dateCreated',
            field=models.DateTimeField(default=utils.timezone.now()),
        ),
        migrations.RenameModel('ChecklistTodos','ChecklistTodo')
    ]
