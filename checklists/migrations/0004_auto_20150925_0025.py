# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0003_auto_20150925_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklisttodos',
            name='dateCreated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
