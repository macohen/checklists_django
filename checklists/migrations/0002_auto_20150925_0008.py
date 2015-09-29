# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='checklistId',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='todoItemId',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
