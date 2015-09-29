# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0011_auto_20150928_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklisttodo',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 0, 36, 7, 589323)),
        ),
    ]
