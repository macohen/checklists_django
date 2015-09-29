# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0004_auto_20150925_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklisttodos',
            name='dateCompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
