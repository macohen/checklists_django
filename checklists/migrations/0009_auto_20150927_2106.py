# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0008_auto_20150927_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklisttodos',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 21, 6, 56, 487224)),
        ),
    ]
