# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0004_auto_20150527_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
