# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='edit_date',
            field=models.DateTimeField(verbose_name='edit'),
        ),
    ]
