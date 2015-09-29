# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0002_auto_20150925_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklisttodos',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 25, 0, 24, 39, 152654)),
        ),
        migrations.AddField(
            model_name='checklisttodos',
            name='dateUpdated',
            field=models.DateTimeField(null=True),
        ),
    ]
